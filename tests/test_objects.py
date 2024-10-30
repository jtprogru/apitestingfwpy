import pytest

from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject


def test_create_object(payload_for_create):
    """
    Test create new object from payload.
    """

    create_object_endpoint = CreateObject()
    create_object_endpoint.create_new_object(payload_for_create)
    create_object_endpoint.check_status_code_is_200ok()
    create_object_endpoint.check_name(payload_for_create["name"])


def test_get_object_by_id(object_id):
    """
    Test get object with specified id.
    """

    get_object_endpoint = GetObject()
    get_object_endpoint.get_object_by_id(object_id)
    get_object_endpoint.check_status_code_is_200ok()
    get_object_endpoint.check_object_id(object_id)


def test_full_update_object(object_id, payload_for_full_update):
    """
    Test update object with specified id with full payload.
    """

    get_object_endpoint = GetObject()
    get_object_endpoint.get_object_by_id(object_id)
    get_object_endpoint.check_status_code_is_200ok()
    get_object_endpoint.check_object_id(object_id)

    update_object_endpoint = UpdateObject()
    update_object_endpoint.full_update_object_by_id(object_id, payload_for_full_update)
    update_object_endpoint.check_status_code_is_200ok()
    update_object_endpoint.check_name(payload_for_full_update["name"])
    update_object_endpoint.check_data_year(payload_for_full_update["data"]["year"])
    update_object_endpoint.check_data_price(payload_for_full_update["data"]["price"])
    update_object_endpoint.check_cpu_model(payload_for_full_update["data"]["CPU model"])
    update_object_endpoint.check_hdd_size(
        payload_for_full_update["data"]["Hard disk size"]
    )


def test_partial_update_object(object_id, payload_for_full_update):
    """
    Test update object with specified id with partial payload.
    """

    get_object_endpoint = GetObject()
    get_object_endpoint.get_object_by_id(object_id)
    get_object_endpoint.check_status_code_is_200ok()
    get_object_endpoint.check_object_id(object_id)

    update_object_endpoint = UpdateObject()
    update_object_endpoint.partial_update_object_by_id(
        object_id, payload_for_full_update
    )
    update_object_endpoint.check_status_code_is_200ok()

    update_object_endpoint.check_name(payload_for_full_update["name"])
    update_object_endpoint.check_data_year(payload_for_full_update["data"]["year"])
    update_object_endpoint.check_data_price(payload_for_full_update["data"]["price"])
    update_object_endpoint.check_cpu_model(payload_for_full_update["data"]["CPU model"])
    update_object_endpoint.check_hdd_size(
        payload_for_full_update["data"]["Hard disk size"]
    )


def test_delete_object(object_id):
    """
    Test that object with specified id is deleted
    """

    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_object_by_id(object_id)
    delete_object_endpoint.check_status_code_is_200ok()
    get_object_endpoint = GetObject()
    get_object_endpoint.get_object_by_id(object_id)
    get_object_endpoint.check_status_code_is_404not_found()
