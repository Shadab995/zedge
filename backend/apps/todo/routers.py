from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .models import Login

router = APIRouter()


@router.post("/", response_description="Add new task")
async def create_user(request: Request, task: Login = Body(...)):
    print("insideeeeeeeee",request)
    print("resp  {}".format(task))
    login_details = jsonable_encoder(task)
    new_login = await request.app.mongodb["users"].insert_one(login_details)
    created_login = await request.app.mongodb["users"].find_one(
        {"_id": new_login.inserted_id}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_login)


@router.get("/", response_description="List all Users")
async def list_users(request: Request):
    users_list = []
    for doc in await request.app.mongodb["users"].find().to_list(length=100):
        users_list.append(doc)
    return users_list


@router.get("/{id}", response_description="Get a single Login User detail")
async def show_user(id: str, request: Request):
    if (task := await request.app.mongodb["users"].find_one({"_id": id})) is not None:
        return task

    raise HTTPException(status_code=404, detail=f"user {id} not found")


# @router.put("/{id}", response_description="Update a task")
# async def update_task(id: str, request: Request, task: UpdateTaskModel = Body(...)):
#     task = {k: v for k, v in task.dict().items() if v is not None}

#     if len(task) >= 1:
#         update_result = await request.app.mongodb["tasks"].update_one(
#             {"_id": id}, {"$set": task}
#         )

#         if update_result.modified_count == 1:
#             if (
#                 updated_task := await request.app.mongodb["tasks"].find_one({"_id": id})
#             ) is not None:
#                 return updated_task

#     if (
#         existing_task := await request.app.mongodb["tasks"].find_one({"_id": id})
#     ) is not None:
#         return existing_task

#     raise HTTPException(status_code=404, detail=f"Task {id} not found")


# @router.delete("/{id}", response_description="Delete Task")
# async def delete_task(id: str, request: Request):
#     delete_result = await request.app.mongodb["tasks"].delete_one({"_id": id})

#     if delete_result.deleted_count == 1:
#         return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

#     raise HTTPException(status_code=404, detail=f"Task {id} not found")