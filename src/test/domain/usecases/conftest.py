import pytest

from src.app.domain.factories.company_factory import CompanyFactory
from src.app.domain.factories.employee_factory import EmployeeFactory
from src.app.domain.factories.entry_factory import EntryFactory
from src.app.domain.requests.create_company_request import CreateCompanyRequest
from src.app.domain.requests.create_employee_request import CreateEmployeeRequest
from src.app.domain.requests.create_entry_request import CreateEntryRequest
from src.app.domain.usecases.commands.create_company import CreateCompany
from src.app.domain.usecases.commands.create_employee import CreateEmployee
from src.app.domain.usecases.commands.create_entry import CreateEntry
from src.app.outgoing_ports.mock_company_repository import MockCompanyRepository
from src.app.outgoing_ports.mock_employee_repository import MockEmployeeRepository
from src.app.outgoing_ports.mock_entry_repository import MockEntryRepository
from src.app.utils.id_generator import IdGenerator


@pytest.fixture
def setup_mock_repositories():
    company_repository = MockCompanyRepository()
    create_company = CreateCompany(company_repository, CompanyFactory(IdGenerator()))

    create_company_request = CreateCompanyRequest(name="Company")
    create_company.handle(create_company_request)

    create_company_request = CreateCompanyRequest(name="Company2")
    create_company.handle(create_company_request)

    employee_repository = MockEmployeeRepository()
    create_employee = CreateEmployee(employee_repository, EmployeeFactory(IdGenerator()), company_repository)

    create_employee_request = CreateEmployeeRequest(name="Employee", salary=1000, company_id=1)
    create_employee.handle(create_employee_request)

    create_employee_request = CreateEmployeeRequest(name="Employee51", salary=4000, company_id=1)
    create_employee.handle(create_employee_request)

    create_employee_request = CreateEmployeeRequest(name="Employee72", salary=5000, company_id=2)
    create_employee.handle(create_employee_request)

    entry_repository = MockEntryRepository()
    create_entry = CreateEntry(entry_repository, EntryFactory(IdGenerator()), employee_repository)

    create_entry_request = CreateEntryRequest(title="Title", content="Content", employee_id=1)
    create_entry.handle(create_entry_request)

    create_entry_request = CreateEntryRequest(title="Title23", content="Content32", employee_id=1)
    create_entry.handle(create_entry_request)

    create_entry_request = CreateEntryRequest(title="Title32", content="Content41", employee_id=1)
    create_entry.handle(create_entry_request)

    create_entry_request = CreateEntryRequest(title="Title34", content="Content09", employee_id=2)
    create_entry.handle(create_entry_request)

    create_entry_request = CreateEntryRequest(title="Title35", content="Content82", employee_id=2)
    create_entry.handle(create_entry_request)

    return company_repository, employee_repository, entry_repository
