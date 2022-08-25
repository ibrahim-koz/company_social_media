import pytest

from src.app.domain.exceptions.employee_not_found_exception import EmployeeNotFoundException
from src.app.domain.factories.company_factory import CompanyFactory
from src.app.domain.factories.employee_factory import EmployeeFactory
from src.app.domain.factories.entry_factory import EntryFactory
from src.app.domain.requests.create_company_request import CreateCompanyRequest
from src.app.domain.requests.create_employee_request import CreateEmployeeRequest
from src.app.domain.usecases.commands.create_company import CreateCompany
from src.app.domain.usecases.commands.create_employee import CreateEmployee
from src.app.domain.usecases.commands.create_entry import CreateEntry
from src.app.outgoing_ports.mock_company_repository import MockCompanyRepository
from src.app.outgoing_ports.mock_employee_repository import MockEmployeeRepository
from src.app.outgoing_ports.mock_entry_repository import MockEntryRepository
from src.app.utils.id_generator import IdGenerator
from src.app.domain.requests.create_entry_request import CreateEntryRequest


@pytest.fixture
def create_entry_fixture():
    entry_factory = EntryFactory(IdGenerator())
    entry_repository = MockEntryRepository()

    company_factory = CompanyFactory(IdGenerator())
    company_repository = MockCompanyRepository()
    create_company = CreateCompany(company_repository, company_factory)
    create_company.handle(CreateCompanyRequest(name="Company"))

    employee_factory = EmployeeFactory(IdGenerator())
    employee_repository = MockEmployeeRepository()
    create_employee = CreateEmployee(employee_repository, employee_factory, company_repository)
    create_employee.handle(CreateEmployeeRequest(name="Employee", salary=1000, company_id=1))

    create_entry = CreateEntry(entry_repository, entry_factory, employee_repository)
    return create_entry, entry_repository, employee_repository


def test_handle(create_entry_fixture):
    create_entry, entry_repository, employee_repository = create_entry_fixture
    _employee_id = 1
    create_entry_request = CreateEntryRequest(title="Title", content="Content", employee_id=_employee_id)
    create_entry.handle(create_entry_request)
    entry = entry_repository.filter(lambda _entry: _entry.title == "Title")[0]
    assert employee_repository.get_employee_by_id(
        _employee_id).has_entry(entry.id)


def test_handle_when_employee_is_absent(create_entry_fixture):
    create_entry, entry_repository, employee_repository = create_entry_fixture
    _employee_id = 0
    create_entry_request = CreateEntryRequest(title="Title", content="Content", employee_id=_employee_id)
    with pytest.raises(EmployeeNotFoundException):
        create_entry.handle(create_entry_request)
