from fastapi import APIRouter, HTTPException
from app.models.plan import PlanCreate, PlanResponse
from app.db.plan_crud import create_plan, get_plan_by_id

router = APIRouter()

@router.post("/plans", response_model=PlanResponse)
async def create_new_plan(plan: PlanCreate):
    plan_id = create_plan(plan.dict())
    return PlanResponse(id=plan_id, **plan.dict())

@router.get("/plans/{plan_id}", response_model=PlanResponse)
async def read_plan(plan_id: str):
    plan = get_plan_by_id(plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="El plan no existe")
    return plan
