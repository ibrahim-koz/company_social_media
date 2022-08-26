class ReadCompany:
    def __init__(self, company_repository):
        self.company_repository = company_repository

    def handle(self, read_company_request):
        id = read_company_request.id
        return self.company_repository.get_company_by_id(id)
