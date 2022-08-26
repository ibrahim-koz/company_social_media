import pytest

from src.app.domain.exceptions.company_not_found_exception import CompanyNotFoundException
from src.app.domain.requests.update_employee_request import UpdateEmployeeRequest
from src.app.domain.usecases.commands.update_employee import UpdateEmployee


@pytest.fixture
def update_employee_fixture(setup_mock_repositories):
    company_repository, employee_repository, _ = setup_mock_repositories
    update_employee = UpdateEmployee(employee_repository, company_repository)
    return update_employee, employee_repository


def test_handle(update_employee_fixture):
    update_employee, employee_repository = update_employee_fixture
    employee_id = 1
    name = "Edsger W. Dijkstra"
    salary = 2000
    company_id = 2
    update_employee_request = UpdateEmployeeRequest(employee_id, name, salary, company_id)
    update_employee.handle(update_employee_request)
    employee = employee_repository.get_employee_by_id(employee_id)
    assert employee.name == name
    assert employee.salary == salary
    assert employee.company_id == company_id


def test_handle_company_not_found(update_employee_fixture):
    update_employee, _ = update_employee_fixture
    employee_id = 1
    name = "Edsger W. Dijkstra"
    salary = 2000
    company_id = 0
    update_employee_request = UpdateEmployeeRequest(employee_id, name, salary, company_id)

    with pytest.raises(CompanyNotFoundException):
        update_employee.handle(update_employee_request)


def test_handle_fields_not_changed(update_employee_fixture):
    update_employee, employee_repository = update_employee_fixture
    employee_id = 1
    update_employee_request = UpdateEmployeeRequest(employee_id)
    update_employee.handle(update_employee_request)
    employee = employee_repository.get_employee_by_id(employee_id)
    assert employee.name == "Employee"
    assert employee.salary == 1000
    assert employee.company_id == 1
