import pytest

from src.app.domain.factories.company_factory import CompanyFactory
from src.app.domain.requests.create_company_request import CreateCompanyRequest
from src.app.domain.usecases.commands.create_company import CreateCompany
from src.app.outgoing_ports.mock_company_repository import MockCompanyRepository
from src.app.utils.id_generator import IdGenerator


@pytest.fixture
def create_company_fixture():
    company_factory = CompanyFactory(IdGenerator())
    company_repository = MockCompanyRepository()
    create_company = CreateCompany(company_repository, company_factory)
    return create_company, company_repository


def test_handle(create_company_fixture):
    create_company, company_repository = create_company_fixture
    create_company_request = CreateCompanyRequest(name="Company")

    create_company.handle(create_company_request)
    assert len(company_repository.filter(lambda company: company.name == "Company")) != 0
