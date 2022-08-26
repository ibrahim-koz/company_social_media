import pytest

from src.app.domain.requests.get_feed_request import GetFeedRequest
from src.app.domain.usecases.queries.get_feed import GetFeed


@pytest.fixture
def get_feed_fixture(setup_mock_repositories):
    company_repository, employee_repository, entry_repository = setup_mock_repositories
    return GetFeed(company_repository, employee_repository, entry_repository)


def test_get_feed(get_feed_fixture):
    get_feed = get_feed_fixture
    company_id = 1
    get_feed_request = GetFeedRequest(company_id)
    entries = get_feed.handle(get_feed_request)
    assert len(entries) == 5
