class UpdateCompany:
    def __init__(self, company_repository):
        self.company_repository = company_repository

    def handle(self, update_company_request):
        id = update_company_request.id
        name = update_company_request.name
        company = self.company_repository.get_company_by_id(id)
        if name is not None:
            company.change_name(name)
        self.company_repository.update(company)