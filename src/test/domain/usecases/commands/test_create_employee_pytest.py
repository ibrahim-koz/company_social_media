import pytest

from src.app.domain.exceptions.company_not_found_exception import CompanyNotFoundException
from src.app.domain.factories.company_factory import CompanyFactory
from src.app.domain.factories.employee_factory import EmployeeFactory
from src.app.domain.requests.create_company_request import CreateCompanyRequest
from src.app.domain.requests.create_employee_request import CreateEmployeeRequest
from src.app.domain.usecases.commands.create_company import CreateCompany
from src.app.domain.usecases.commands.create_employee import CreateEmployee
from src.app.outgoing_ports.mock_company_repository import MockCompanyRepository
from src.app.outgoing_ports.mock_employee_repository import MockEmployeeRepository
from src.app.utils.id_generator import IdGenerator


@pytest.fixture
def create_employee_fixture():
    employee_factory = EmployeeFactory(IdGenerator())
    employee_repository = MockEmployeeRepository()

    company_factory = CompanyFactory(IdGenerator())
    company_repository = MockCompanyRepository()
    create_company = CreateCompany(company_repository, company_factory)
    create_company.handle(CreateCompanyRequest(name="Company"))

    create_employee = CreateEmployee(employee_repository, employee_factory, company_repository)
    return create_employee, employee_repository, company_repository


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
