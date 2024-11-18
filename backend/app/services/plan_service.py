# from bson import ObjectId  
# from app.models.plan import Plan
# from app.db.mongo import db

# class PlanService:
#     @staticmethod
#     def get_all_plans():
#         return list(db["plans"].find({}))

#     @staticmethod
#     def create_plan(plan: Plan):
#         db["plans"].insert_one(plan.dict())
#         return plan

#     @staticmethod
#     def update_plan(plan_id: str, plan: Plan):
#         # Convertir el plan_id a ObjectId
#         object_id = ObjectId(plan_id)
#         # Actualizar solo los campos no nulos
#         update_data = {k: v for k, v in plan.dict().items() if v is not None}

#         result = db["plans"].update_one({"_id": object_id}, {"$set": update_data})
#         if result.matched_count == 0:
#             raise HTTPException(status_code=404, detail="Plan not found")
#         return plan

#     @staticmethod
#     def delete_plan(plan_id: str):
#         object_id = ObjectId(plan_id)  # Convertir el plan_id a ObjectId
#         result = db["plans"].delete_one({"_id": object_id})
#         if result.deleted_count == 0:
#             raise HTTPException(status_code=404, detail="Plan not found")
#         return {"message": "Plan deleted successfully"}

from app.db.plan_crud import create_plan, get_plan_by_id, get_all_plans, update_plan, delete_plan

class PlanService:
    @staticmethod
    def create_plan(plan_data):
        return create_plan(plan_data)

    @staticmethod
    def get_plan_by_id(plan_id):
        return get_plan_by_id(plan_id)

    @staticmethod
    def get_all_plans():
        return get_all_plans()

    @staticmethod
    def update_plan(plan_id, updated_data):
        return update_plan(plan_id, updated_data)

    @staticmethod
    def delete_plan(plan_id):
        return delete_plan(plan_id)
