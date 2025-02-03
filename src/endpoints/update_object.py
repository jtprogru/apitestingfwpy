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
            url=f"{self.base_url}/{object_id}",
            json=payload,
            timeout=self.timeout,
        )
        self.response_json = self.response.json()

    def partial_update_object_by_id(self, object_id: str, payload: dict) -> None:
        """
        Метод для частичного обновления объекта по ID.
        """
        self.response = requests.patch(
            f"{self.base_url}/{object_id}",
            json=payload,
            timeout=self.timeout,
        )
        self.response_json = self.response.json()

    def check_data_price(self, price: float) -> None:
        """
        Проверка изменения цены.
        """

        assert (
            self.response_json["data"]["price"] == price
        ), f"Object price is {self.response_json['data']['price']}, expected {price}"

    def check_data_year(self, year: int) -> None:
        """
        Проверка изменения года.
        """

        assert (
            self.response_json["data"]["year"] == year
        ), f"Object year is {self.response_json['data']['year']}, expected {year}"

    def check_cpu_model(self, cpu_model: str) -> None:
        """
        Проверка изменения модели процессора.
        """

        assert (
            self.response_json["data"]["CPU model"] == cpu_model
        ), f"Object CPU model is {self.response_json['data']['CPU model']}, expected {cpu_model}"

    def check_hdd_size(self, hdd_size: str) -> None:
        """
        Проверка изменения размера жесткого диска.
        """

        assert (
            self.response_json["data"]["Hard disk size"] == hdd_size
        ), f"Object Hard disk size is {self.response_json['data']['Hard disk size']}, expected {hdd_size}"
