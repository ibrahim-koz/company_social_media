class CreateCompany:
    def __init__(self, company_repository, company_factory):
        self.company_repository = company_repository
        self.company_factory = company_factory

    def handle(self, create_company_request):
        name = create_company_request.name
        new_company = self.company_factory.create(name)
        self.company_repository.add(new_company)
