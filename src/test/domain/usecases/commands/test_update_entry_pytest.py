import pytest

from src.app.domain.exceptions.entry_not_found_exception import EntryNotFoundException
from src.app.domain.requests.update_entry_request import UpdateEntryRequest
from src.app.domain.usecases.commands.update_entry import UpdateEntry


@pytest.fixture
def update_entry_fixture(setup_mock_repositories):
    _, _, entry_repository = setup_mock_repositories
    update_entry = UpdateEntry(entry_repository)
    return update_entry, entry_repository


def test_handle(update_entry_fixture):
    update_entry, entry_repository = update_entry_fixture
    entry_id = 1
    title = "Updated Title"
    content = "Updated Content"
    update_entry_request = UpdateEntryRequest(entry_id, title, content)
    update_entry.handle(update_entry_request)
    entry = entry_repository.get_entry_by_id(entry_id)
    assert entry.title == title
    assert entry.content == content


def test_handle_not_found_entry(update_entry_fixture):
    update_entry, _ = update_entry_fixture
    entry_id = 0
    title = "Updated Title"
    content = "Updated Content"
    update_entry_request = UpdateEntryRequest(entry_id, title, content)

    with pytest.raises(EntryNotFoundException):
        update_entry.handle(update_entry_request)


def test_handle_title_not_set(update_entry_fixture):
    update_entry, entry_repository = update_entry_fixture
    entry_id = 1
    content = "Updated Content"
    update_entry_request = UpdateEntryRequest(id=entry_id, content=content)
    update_entry.handle(update_entry_request)

    entry = entry_repository.get_entry_by_id(entry_id)
    assert entry.title == "Title"
    assert entry.content == content


def test_handle_content_not_set(update_entry_fixture):
    update_entry, entry_repository = update_entry_fixture
    entry_id = 1
    title = "Updated Title"
    update_entry_request = UpdateEntryRequest(id=entry_id, title=title)
    update_entry.handle(update_entry_request)

    entry = entry_repository.get_entry_by_id(entry_id)
    assert entry.title == title
    assert entry.content == "Content"
