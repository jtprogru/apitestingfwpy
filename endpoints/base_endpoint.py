import requests


class BaseEndpoint:
    """
    Базовый класс для работы с API.
    """

    def __init__(self) -> None:
        self.base_url: str = "https://api.restful-api.dev/objects"
        self.response: requests.Response | None = None
        self.response_json: dict | None = None
        self.timeout: int = 15

    def check_status_code_is_200ok(self) -> None:
        """
        Проверка статус кода 200 OK.
        """

        assert (
            self.response.status_code == 200
        ), f"Status code is {self.response.status_code}, expected 200 OK"

    def check_name(self, name: str) -> None:
        """
        Проверка имени объекта.
        """

        assert (
            self.response_json["name"] == name
        ), f"Object Name is {self.response_json['name']}, expected {name}"

    def check_object_id(self, object_id: str) -> None:
        """
        Проверка ID объекта.
        """

        assert (
            self.response_json["id"] == object_id
        ), f"Object ID is {self.response_json['id']}, expected {object_id}"
