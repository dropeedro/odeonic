# from app.db.mongo import db

# def create_plan(plan_data):
#     result = db.plans.insert_one(plan_data)
#     return str(result.inserted_id)

# def get_plan_by_id(plan_id):
#     return db.plans.find_one({"_id": plan_id})


from app.db.mongo import db

def create_plan(plan_data):
    # Asegúrate de que 'features' esté incluido en los datos
    result = db.plans.insert_one(plan_data)
    return str(result.inserted_id)

def get_plan_by_id(plan_id):
    return db.plans.find_one({"_id": plan_id})

def get_all_plans():
    # Devuelve todos los planes, incluyendo el nuevo campo
    return list(db.plans.find())

def update_plan(plan_id, updated_data):
    db.plans.update_one({"_id": plan_id}, {"$set": updated_data})
    return get_plan_by_id(plan_id)

def delete_plan(plan_id):
    db.plans.delete_one({"_id": plan_id})
    return True
