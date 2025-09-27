from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUsersRequestSchema, CreateUserResponseSchema
from clients.users.private_users_client import get_private_users_client
from clients.private_http_builder import AuthenticationUserSchema
import pytest
from pydantic import BaseModel, EmailStr


class UserFixture(BaseModel):
    request: CreateUsersRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email
    
    @property
    def password(self) -> str:
        return self.request.password
    
    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(
            email=self.request.email,
            password=self.request.password
        )


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUsersRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)


@pytest.fixture
def private_users_client(function_user: UserFixture):
    return get_private_users_client(function_user.authentication_user)
