import pytest

from src.app.domain.requests.read_employee_request import ReadEmployeeRequest
from src.app.domain.usecases.queries.read_employee import ReadEmployee


@pytest.fixture
def read_employee_fixture(setup_mock_repositories):
    _, employee_repository, _ = setup_mock_repositories
    return ReadEmployee(employee_repository)


def test_read_employee(read_employee_fixture):
    read_employee = read_employee_fixture
    read_employee_request = ReadEmployeeRequest(id=2)
    employee = read_employee.handle(read_employee_request)
    assert employee.name == "Employee51"
    assert employee.salary == 4000
    assert employee.company_id == 1