from fastapi import APIRouter, Depends, status
from fastapi_users import FastAPIUsers
from app.auth.manager import get_user_manager
from app.auth.auth import auth_backend
from app.auth.schemas import UserRead, UserCreate, CodeRead
from app.auth.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from app.auth.services import generate_code
from app.auth.dependencies import valid_invitation_code

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
)

authRouter.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    dependencies=[Depends(valid_invitation_code)]
)

current_user = fastapi_users.current_user()


@authRouter.get('/me', response_model=UserRead, status_code=status.HTTP_200_OK)
def me(user: User = Depends(current_user)):
    return UserRead.from_orm(user)


@authRouter.post('/code', response_model=CodeRead, status_code=status.HTTP_200_OK)
async def generate_new_code(user: User = Depends(current_user), db: AsyncSession = Depends(get_async_session)):
    return await generate_code(user=user, db=db)
