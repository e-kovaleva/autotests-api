from clients.users.public_users_client import get_public_users_client
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.users_schema import CreateUsersRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from http import HTTPStatus
import pytest


@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    public_users_client = get_public_users_client()
    authentication_users_client = get_authentication_client()

    request_create_user = CreateUsersRequestSchema()
    response_create_user = public_users_client.create_user(request_create_user)

    request_login = LoginRequestSchema(
        email=request_create_user.email,
        password=request_create_user.password
    )
    response_login = authentication_users_client.login_api(request_login)
    response_login_data = LoginResponseSchema.model_validate_json(response_login.text)

    assert_status_code(response_login.status_code, HTTPStatus.OK)
    assert_login_response(response_login_data)
    validate_json_schema(instance=response_login.json(), schema=response_login_data.model_json_schema())
