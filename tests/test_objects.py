import pytest

from endpoints.create_object import CreateObject


def test_create_object(payload_for_create):
    create_object_endpoint = CreateObject()
    create_object_endpoint.create_new_object(payload_for_create)
    create_object_endpoint.check_status_code_is_200ok()
    create_object_endpoint.check_name(payload_for_create["name"])
