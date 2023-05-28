from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from app.auth.manager import get_user_manager
from app.auth.auth import auth_backend
from app.auth.schemas import UserRead, UserCreate
from app.auth.models import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

authRouter = APIRouter(
    prefix='/auth',
    tags=['auth']
)

authRouter.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt"
)

authRouter.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate)
)
