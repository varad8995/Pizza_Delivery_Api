from pydantic import BaseModel
from typing import Optional
class Signup(BaseModel):
    id :Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                       "username" :"john doe",
                       "email" :"john@gmail.com",
                       "password":"pasword",
                       "is_staff":"False",
                       "is_active":"True"
            
        }
        }


class Settings(BaseModel):
    authjwt_secret_key:str="44ad4c4e0f60e5a5ace84ec3e3e7675fa04ea1642bc5f8f5669ad12090b7737b"


class LoginModel(BaseModel):
    username :str
    password : str    


class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str] ="PENDING"
    pizza_size:Optional[str] = "SMALL"
    user_id:Optional[int]
   

    class Config:

        orm_mode = True
        schema_extra = {
            'example':{
                       "quantity" :2,
                       "pizza_size" :"LARGE",
                    
        }
        }


class OrderStatusModel(BaseModel):
    order_status:Optional[str]="PENDING"

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }