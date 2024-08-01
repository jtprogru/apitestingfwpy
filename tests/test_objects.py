import pytest

from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject


def test_create_object(payload_for_create):
    create_object_endpoint = CreateObject()
    create_object_endpoint.create_new_object(payload_for_create)
    create_object_endpoint.check_status_code_is_200ok()
    create_object_endpoint.check_name(payload_for_create["name"])


def test_get_object(object_id):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_object_by_id(object_id)
    get_object_endpoint.check_status_code_is_200ok()
    get_object_endpoint.check_object_id(object_id)
