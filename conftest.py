import pytest

from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject


@pytest.fixture
def payload_for_create():
    """
    Стандартный набор данных для создания объекта.
    """
    return {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2000.00,
            "CPU model": "Apple M1",
            "Hard disk size": "1 TB",
        },
    }


@pytest.fixture
def payload_for_full_update():
    """
    Стандартный набор данных для полного обновления объекта.
    """
    return {
        "name": "Apple MacBook Pro 14",
        "data": {
            "year": 2024,
            "price": 5000.00,
            "CPU model": "Apple M4 Max",
            "Hard disk size": "8 TB",
        },
    }


@pytest.fixture
def payload_for_partially_update():
    """
    Стандартный набор данных для частичного обновления объекта.
    """
    return {
        "data": {
            "year": 2020,
            "price": 2500.00,
        },
    }


@pytest.fixture
def object_id(payload_for_create):
    """
    Фикстура для получения ID созданного объекта и последующего удаления тестовых данных с использованием фреймворка.
    """
    create_object_endpoint = CreateObject()
    create_object_endpoint.create_new_object(payload_for_create)
    object_id = create_object_endpoint.response_json["id"]

    yield object_id

    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_object_by_id(object_id)
