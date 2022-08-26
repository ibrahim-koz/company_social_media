import pytest

from src.app.domain.exceptions.employee_not_found_exception import EmployeeNotFoundException
from src.app.domain.requests.delete_employee_request import DeleteEmployeeRequest
from src.app.domain.usecases.commands.delete_employee import DeleteEmployee
from src.app.domain.usecases.commands.delete_entry import DeleteEntry


@pytest.fixture
def delete_employee_fixture(setup_mock_repositories):
    company_repository, employee_repository, entry_repository = setup_mock_repositories
    delete_entry = DeleteEntry(employee_repository, entry_repository)
    delete_employee = DeleteEmployee(company_repository, employee_repository, delete_entry)
    return delete_employee, company_repository, employee_repository


def test_handle(delete_employee_fixture):
    delete_employee, company_repository, employee_repository = delete_employee_fixture
    employee_id = 1
    delete_employee_request = DeleteEmployeeRequest(employee_id)
    employee = employee_repository.get_employee_by_id(employee_id)

    delete_employee.handle(delete_employee_request)
    assert not company_repository.get_company_by_id(employee.company_id).has_employee(employee_id)


def test_handle_not_found_employee(delete_employee_fixture):
    delete_employee, _, _ = delete_employee_fixture
    employee_id = 0
    delete_employee_request = DeleteEmployeeRequest(employee_id)

    with pytest.raises(EmployeeNotFoundException):
        delete_employee.handle(delete_employee_request)
