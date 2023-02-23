from fastapi import APIRouter
from model.user import User
from schemas.login import Login
from typing import List

router = APIRouter()

@router.post('/user/login')
def sign_in(user:Login):
    """User login"""
    user = user.dict()
    query = User.select().where(
        (User.code == user['code']) & (User.password == user['password'])).dicts()
    query_len = list(query)
    if len(query_len):
        return {"code": 200, "data": query_len}
    else:
        return {"code": 400, "data": query_len}