import pytest

from src.app.domain.usecases.queries.get_timeline import GetTimeline


@pytest.fixture
def get_timeline_fixture(setup_mock_repositories):
    company_repository, employee_repository, entry_repository = setup_mock_repositories
    return GetTimeline(employee_repository, entry_repository)


def test_get_timeline(get_timeline_fixture):
    get_timeline = get_timeline_fixture
    employee_id = 2
    entries = get_timeline.handle(employee_id)
    assert len(entries) == 2
