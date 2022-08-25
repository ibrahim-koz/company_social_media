from src.app.domain.exceptions.company_not_found_exception import CompanyNotFoundException
from src.app.domain.repositories.company_repository import CompanyRepository


class MockCompanyRepository(CompanyRepository):
    def __init__(self):
        self.companies = {}

    def add(self, company):
        self.companies[company.id] = company

    def get_company_by_id(self, id):
        try:
            return self.companies[id]
        except KeyError:
            raise CompanyNotFoundException()

    def filter(self, function):
        return list(filter(function, self.companies.values()))

    def update(self, company):
        self.companies[company.id] = company
