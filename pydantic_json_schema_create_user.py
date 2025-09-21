from clients.users.public_users_client import get_public_users_client
from tools.fakers import fake
from clients.users.users_schema import CreateUsersRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema


public_users_client = get_public_users_client()

create_user_request = CreateUsersRequestSchema(
    email=fake.email(),
    password='string',
    last_name='string',
    first_name='string',
    middle_name='string'
)

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)
