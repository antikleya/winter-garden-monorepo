from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy
from app.config import JWT_TOKEN

cookie_transport = CookieTransport(cookie_max_age=15552000)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=JWT_TOKEN, lifetime_seconds=15552000)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
