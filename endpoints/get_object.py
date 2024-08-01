import requests

from endpoints.base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):
    """
    Класс для получения объекта по ID.
    """

    def __init__(self) -> None:
        super().__init__()

    def get_object_by_id(self, object_id: str) -> None:
        """
        Метод для получения объекта по ID.
        """

        self.response = requests.get(
            f"{self.base_url}/{object_id}",
        )
        self.response_json = self.response.json()

        return

    def check_status_code_is_404not_found(self) -> None:
        """
        Проверка статус кода 404 NOT FOUND.
        """

        assert self.response.status_code == 404
