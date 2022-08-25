def test_handle(create_company_fixture):
    create_company, company_repository = create_company_fixture
    create_company_request = {"name": "Company"}
    create_company.handle(create_company_request)
    assert len(company_repository.filter(lambda company: company.name == "Company")) != 0
