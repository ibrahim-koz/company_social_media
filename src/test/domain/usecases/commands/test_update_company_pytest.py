import pytest

from src.app.domain.requests.update_company_request import UpdateCompanyRequest
from src.app.domain.usecases.commands.update_company import UpdateCompany


@pytest.fixture
def update_company_fixture(setup_mock_repositories):
    company_repository, _, _ = setup_mock_repositories
    update_company = UpdateCompany(company_repository)
    return update_company, company_repository


def test_update_company_handle(update_company_fixture):
    update_company, company_repository = update_company_fixture
    update_company_request = UpdateCompanyRequest(1, "New Name")
    update_company.handle(update_company_request)
    assert company_repository.get_company_by_id(1).name == "New Name"
