from fastapi import APIRouter
from router import user , login

router = APIRouter()

router.include_router(
    user.router,
    prefix= '/user',
    tags=['User']
)
router.include_router(
    login.router,
    prefix= '/user',
    tags=['Login']
)

# router.include_router(
#     student.router,
#     prefix= '/student',
#     tags=['Student']
# )