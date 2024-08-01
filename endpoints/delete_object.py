import requests

from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    """
    Класс для удаления объекта по ID.
    """

    def __init__(self) -> None:
        super().__init__()

    def delete_object_by_id(self, object_id: str) -> None:
        """
        Метод для удаления объекта по ID.
        """

        self.response = requests.delete(
            f"{self.base_url}/{object_id}",
        )

        return
