import pytest

from src.app.domain.requests.read_company_request import ReadCompanyRequest
from src.app.domain.usecases.queries.read_company import ReadCompany


@pytest.fixture
def read_company_fixture(setup_mock_repositories):
    company_repository, _, _ = setup_mock_repositories
    return ReadCompany(company_repository)


def test_read_company(read_company_fixture):
    read_company = read_company_fixture
    read_company_request = ReadCompanyRequest(1)
    company = read_company.handle(read_company_request)
    assert company.name == "Company"
