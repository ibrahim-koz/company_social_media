from src.app.domain.repositories.company_repository import CompanyRepository


class MockCompanyRepository(CompanyRepository):
    def __init__(self):
        self.companies = {}

    def add(self, company):
        self.companies[company.id] = company

    def get_company_by_id(self, id):
        return self.companies[id]

    def filter(self, function):
        return [function(company) for company in self.companies.values()]