from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient


class PublicUsersRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    def create_user_api(self, request: PublicUsersRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с необходимыми данными.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/users', json=request)
