import pytest

from src.app.domain.exceptions.company_not_found_exception import CompanyNotFoundException
from src.app.domain.requests.create_employee_request import CreateEmployeeRequest


def test_handle(create_employee_fixture):
    create_employee, employee_repository, company_repository = create_employee_fixture
    _company_id = 1
    create_employee_request = CreateEmployeeRequest(name="Employee", salary=1000, company_id=1)
    create_employee.handle(create_employee_request)
    employee = employee_repository.filter(lambda _employee: _employee.name == "Employee")[0]
    assert company_repository.get_company_by_id(_company_id).has_employee(employee.id)


def test_handle_fail_when_company_is_absent(create_employee_fixture):
    create_employee, employee_repository, _ = create_employee_fixture
    create_employee_request = CreateEmployeeRequest(name="Employee", salary=1000, company_id=0)
    with pytest.raises(CompanyNotFoundException):
        create_employee.handle(create_employee_request)
