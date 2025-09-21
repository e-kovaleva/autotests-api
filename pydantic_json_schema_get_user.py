from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client, AuthenticationUserSchema
from tools.fakers import get_random_email
from clients.users.users_schema import CreateUsersRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema


public_users_client = get_public_users_client()

create_user_request = CreateUsersRequestSchema(
    email=get_random_email(),
    password='string',
    last_name='string',
    first_name='string',
    middle_name='string'
)

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_json = create_user_response.json()

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user_api(create_user_response_json['user']['id'])
get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)
