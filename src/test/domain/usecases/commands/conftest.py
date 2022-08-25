import pytest

from src.app.domain.factories.company_factory import CompanyFactory
from src.app.domain.usecases.commands.create_company import CreateCompany
from src.app.outgoing_ports.MockCompanyRepository import MockCompanyRepository
from src.app.utils.id_generator import IdGenerator


@pytest.fixture
def create_company_fixture():
    company_factory = CompanyFactory(IdGenerator())
    company_repository = MockCompanyRepository()
    create_company = CreateCompany(company_repository, company_factory)
    return create_company, company_repository
