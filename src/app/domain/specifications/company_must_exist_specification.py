from src.app.domain.exceptions.company_not_found_exception import CompanyNotFoundException


class CompanyMustExistSpecification:
    def __init__(self, company_repository):
        self.company_repository = company_repository

    def is_satisfied_by(self, company_id):
        try:
            self.company_repository.get_company_by_id(company_id)
            return True
        except CompanyNotFoundException:
            return False
