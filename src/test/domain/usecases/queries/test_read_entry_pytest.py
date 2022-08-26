import pytest

from src.app.domain.requests.read_entry_request import ReadEntryRequest
from src.app.domain.usecases.queries.read_entry import ReadEntry


@pytest.fixture
def read_entry_fixture(setup_mock_repositories):
    _, _, entry_repository = setup_mock_repositories
    return ReadEntry(entry_repository)


def test_read_entry(read_entry_fixture):
    read_entry = read_entry_fixture
    read_entry_request = ReadEntryRequest(id=3)
    entry = read_entry.handle(read_entry_request)
    assert entry.title == "Title32"
    assert entry.content == "Content41"
    assert entry.employee_id == 1
