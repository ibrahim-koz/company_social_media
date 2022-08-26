import pytest

from src.app.domain.exceptions.company_not_found_exception import CompanyNotFoundException
from src.app.domain.requests.delete_company_request import DeleteCompanyRequest
from src.app.domain.usecases.commands.delete_company import DeleteCompany
from src.app.domain.usecases.commands.delete_employee import DeleteEmployee
from src.app.domain.usecases.commands.delete_entry import DeleteEntry


@pytest.fixture
def delete_company_fixture(setup_mock_repositories):
    company_repository, employee_repository, entry_repository = setup_mock_repositories
    delete_entry = DeleteEntry(employee_repository, entry_repository)
    delete_employee = DeleteEmployee(company_repository, employee_repository, delete_entry)
    delete_company = DeleteCompany(company_repository, delete_employee)
    return delete_company, company_repository


def test_handle(delete_company_fixture):
    delete_company, company_repository = delete_company_fixture
    company_id = 1
    delete_company_request = DeleteCompanyRequest(company_id)
    delete_company.handle(delete_company_request)
    with pytest.raises(CompanyNotFoundException):
        company_repository.get_company_by_id(company_id)


def test_handle_not_found_company(delete_company_fixture):
    delete_company, _ = delete_company_fixture
    company_id = 0
    delete_company_request = DeleteCompanyRequest(company_id)

    with pytest.raises(CompanyNotFoundException):
        delete_company.handle(delete_company_request)
