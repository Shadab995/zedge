import uuid
from typing import Optional

from pydantic import BaseModel, Field


class Login(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username : str = Field(...)
    password : str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "username": "shadabbarmare95@gmail.com",
                "password": "Barmare@45",
            }
        }


# class UpdateTaskModel(BaseModel):
#     name: Optional[str]
#     completed: Optional[bool]

#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "My other important task",
#                 "completed": True,
#             }
#         }
