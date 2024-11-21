from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from app.models.plan import Plan
from app.services.plan_service import PlanService
from app.services.user_service import update_subscription
import stripe
import os

# Router initialization
router = APIRouter()

# Stripe configuration
stripe.api_key = os.getenv("STRIPE_API_KEY")  # Load your Stripe API key from environment variables
stripe.log = "debug"

# Price mapping
price_mapping = {
    "personal": "price_1QN3weGY6BYBTtJUr4Zj1sxZ",  # Price ID for Personal plan
    "business": "price_1QN2KIGY6BYBTtJULpFghusG"   # Price ID for Business plan
}

# Models
class SubscriptionRequest(BaseModel):
    plan_id: str
    email: EmailStr

class SubscriptionUpdateRequest(BaseModel):
    user_email: str
    subscription_data: dict

# Plan endpoints
@router.get("/", response_model=list[Plan])
async def get_all_plans():
    return PlanService.get_all_plans()

@router.post("/", response_model=Plan)
async def create_plan(plan: Plan):
    return PlanService.create_plan(plan)

@router.put("/{plan_id}", response_model=Plan)
async def update_plan(plan_id: str, plan: Plan):
    return PlanService.update_plan(plan_id, plan)

@router.delete("/{plan_id}")
async def delete_plan(plan_id: str):
    return PlanService.delete_plan(plan_id)

# Endpoint to create a subscription session
@router.post("/create-subscription-session")
async def create_subscription_session(request: SubscriptionRequest):
    """
    Create a Stripe Checkout session for a subscription.
    """
    print(f"Received data: {request.dict()}")
    price_id = price_mapping.get(request.plan_id)

    if not price_id:
        raise HTTPException(status_code=400, detail="Invalid plan ID")

    try:
        # Create a customer or use the provided email
        customer = stripe.Customer.create(email=request.email)

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="subscription",
            line_items=[
                {"price": price_id, "quantity": 1},
            ],
            customer=customer.id,  # Associate the session with the customer
            success_url="http://localhost:5173/dashboard?success=true",
            cancel_url="http://localhost:5173/dashboard?canceled=true",
        )
        print(f"Session successfully created: {session.url}")
        return {"url": session.url}
    except stripe.error.StripeError as e:
        print(f"Error in Stripe: {e}")
        raise HTTPException(status_code=500, detail=f"Stripe error: {str(e)}")

# Endpoint to validate a price
@router.post("/validate-price")
async def validate_price(price_id: str):
    """
    Validate if a price exists in Stripe.
    """
    try:
        price = stripe.Price.retrieve(price_id)
        return {"valid": True, "price": price}
    except stripe.error.InvalidRequestError as e:
        return {"valid": False, "error": str(e)}

# Endpoint to update subscription manually for testing
@router.post("/update-subscription")
async def test_update_subscription(request: SubscriptionUpdateRequest):
    """
    Update subscription data for a user in MongoDB.
    """
    try:
        result = update_subscription(request.user_email, request.subscription_data)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
