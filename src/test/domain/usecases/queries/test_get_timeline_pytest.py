import pytest

from src.app.domain.requests.get_timeline_request import GetTimelineRequest
from src.app.domain.usecases.queries.get_timeline import GetTimeline


@pytest.fixture
def get_timeline_fixture(setup_mock_repositories):
    company_repository, employee_repository, entry_repository = setup_mock_repositories
    return GetTimeline(employee_repository, entry_repository)


def test_get_timeline(get_timeline_fixture):
    get_timeline = get_timeline_fixture
    employee_id = 2
    get_timeline_request = GetTimelineRequest(employee_id)
    entries = get_timeline.handle(get_timeline_request)
    assert len(entries) == 2
