import requests

from endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):
    """
    Класс для создания нового объекта.
    """

    def __init__(self) -> None:
        super().__init__()

    def create_new_object(self, payload: dict) -> None:
        """
        Метод для создания нового объекта.
        :param payload:
        :return:
        """

        self.response = requests.post(
            f"{self.base_url}",
            json=payload,
        )
        self.response_json = self.response.json()

        return
