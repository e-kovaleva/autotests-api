from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUsersRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    def create_user_api(self, request: CreateUsersRequestSchema) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с необходимыми данными.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            '/api/v1/users',
            json=request.model_dump(by_alias=True)
        )
    
    def create_user(self, request: CreateUsersRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)
    

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
