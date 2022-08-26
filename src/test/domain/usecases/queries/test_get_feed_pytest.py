import pytest

from src.app.domain.usecases.queries.get_feed import GetFeed


@pytest.fixture
def get_feed_fixture(setup_mock_repositories):
    company_repository, employee_repository, entry_repository = setup_mock_repositories
    return GetFeed(company_repository, employee_repository, entry_repository)


def test_get_feed(get_feed_fixture):
    company_id = 1
    entries = get_feed_fixture.handle(company_id)
    assert len(entries) == 3
