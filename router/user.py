from fastapi import APIRouter
from model.user import User
from schemas import user as userschemas
from typing import List
from playhouse.shortcuts import model_to_dict

router = APIRouter()

@router.get('/read', response_model=List[userschemas.User])
def get_account():
    return list(User.select())

@router.post('/create')
def create_account(user:userschemas.UserCreate):
    return model_to_dict(User.create(**user.dict()))