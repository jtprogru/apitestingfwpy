import requests

from endpoints.base_endpoint import BaseEndpoint


class UpdateObject(BaseEndpoint):
    """
    Класс для обновления объекта.
    """

    def __init__(self) -> None:
        super().__init__()

    def full_update_object_by_id(self, object_id: str, payload: dict) -> None:
        """
        Метод для полного обновления объекта по ID.
        """

        self.response = requests.put(
            f"{self.base_url}/{object_id}",
            json=payload,
        )
        self.response_json = self.response.json()

        return

    def partial_update_object_by_id(self, object_id: str, payload: dict) -> None:
        """
        Метод для частичного обновления объекта по ID.
        """
        self.response = requests.patch(
            f"{self.base_url}/{object_id}",
            json=payload,
        )
        self.response_json = self.response.json()

        return

    def check_data_price(self, price: float) -> None:
        """
        Проверка изменения цены.
        """

        assert self.response_json["data"]["price"] == price

    def check_data_year(self, year: int) -> None:
        """
        Проверка изменения года.
        """

        assert self.response_json["data"]["year"] == year

    def check_cpu_model(self, cpu_model: str) -> None:
        """
        Проверка изменения модели процессора.
        """

        assert self.response_json["data"]["CPU model"] == cpu_model

    def check_hdd_size(self, hdd_size: str) -> None:
        """
        Проверка изменения размера жесткого диска.
        """

        assert self.response_json["data"]["Hard disk size"] == hdd_size
