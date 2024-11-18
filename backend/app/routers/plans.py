from fastapi import APIRouter, HTTPException
from app.models.plan import Plan
from app.services.plan_service import PlanService

router = APIRouter()

# @router.get("/", response_model=list[Plan])
# async def get_all_plans():
#     return PlanService.get_all_plans()

# @router.post("/", response_model=Plan)
# async def create_plan(plan: Plan):
#     return PlanService.create_plan(plan)

# @router.put("/{plan_id}", response_model=Plan)
# async def update_plan(plan_id: str, plan: Plan):
#     return PlanService.update_plan(plan_id, plan)

# @router.delete("/{plan_id}")
# async def delete_plan(plan_id: str):
#     return PlanService.delete_plan(plan_id)

@router.post("/", response_model=Plan)
async def create_plan(plan: Plan):
    return PlanService.create_plan(plan.dict())

@router.put("/{plan_id}", response_model=Plan)
async def update_plan(plan_id: str, plan: Plan):
    return PlanService.update_plan(plan_id, plan.dict())
