from src.app.domain.requests.create_company_request import CreateCompanyRequest


def test_handle(create_company_fixture):
    create_company, company_repository = create_company_fixture
    create_company_request = CreateCompanyRequest(name="Company")

    create_company.handle(create_company_request)
    assert len(company_repository.filter(lambda company: company.name == "Company")) != 0
