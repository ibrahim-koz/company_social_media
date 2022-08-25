import pytest

from src.app.domain.factories.company_factory import CompanyFactory
from src.app.domain.factories.employee_factory import EmployeeFactory
from src.app.domain.requests.create_company_request import CreateCompanyRequest
from src.app.domain.specifications.company_must_exist_specification import CompanyMustExistSpecification
from src.app.domain.usecases.commands.create_company import CreateCompany
from src.app.domain.usecases.commands.create_employee import CreateEmployee
from src.app.outgoing_ports.mock_company_repository import MockCompanyRepository
from src.app.outgoing_ports.mock_employee_repository import MockEmployeeRepository
from src.app.utils.id_generator import IdGenerator


@pytest.fixture
def create_company_fixture():
    company_factory = CompanyFactory(IdGenerator())
    company_repository = MockCompanyRepository()
    create_company = CreateCompany(company_repository, company_factory)
    return create_company, company_repository


@pytest.fixture
def create_employee_fixture():
    employee_factory = EmployeeFactory(IdGenerator())
    employee_repository = MockEmployeeRepository()

    company_factory = CompanyFactory(IdGenerator())
    company_repository = MockCompanyRepository()
    create_company = CreateCompany(company_repository, company_factory)
    create_company.handle(CreateCompanyRequest(name="Company"))

    company_must_exist_specification = CompanyMustExistSpecification(company_repository)
    create_employee = CreateEmployee(employee_repository, employee_factory, company_must_exist_specification,
                                     company_repository)
    return create_employee, employee_repository, company_repository
