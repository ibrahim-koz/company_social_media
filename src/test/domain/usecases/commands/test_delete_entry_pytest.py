import pytest

from src.app.domain.exceptions.entry_not_found_exception import EntryNotFoundException
from src.app.domain.requests.delete_entry_request import DeleteEntryRequest
from src.app.domain.usecases.commands.delete_entry import DeleteEntry


@pytest.fixture
def delete_entry_fixture(setup_mock_data):
    _, employee_repository, entry_repository = setup_mock_data
    delete_entry = DeleteEntry(employee_repository, entry_repository)
    return delete_entry, employee_repository, entry_repository


def test_handle(delete_entry_fixture):
    delete_entry, employee_repository, entry_repository = delete_entry_fixture
    entry_id = 1
    delete_entry_request = DeleteEntryRequest(entry_id)
    entry = entry_repository.get_entry_by_id(entry_id)

    delete_entry.handle(delete_entry_request)
    assert not employee_repository.get_employee_by_id(entry.employee_id).has_entry(entry_id)
    with pytest.raises(EntryNotFoundException):
        entry_repository.get_entry_by_id(entry_id)


def test_handle_not_found_entry(delete_entry_fixture):
    delete_entry, _, _ = delete_entry_fixture
    entry_id = 0
    delete_entry_request = DeleteEntryRequest(entry_id)

    with pytest.raises(EntryNotFoundException):
        delete_entry.handle(delete_entry_request)
