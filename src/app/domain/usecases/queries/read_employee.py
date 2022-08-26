class ReadEmployee:
    def __init__(self, employee_repository):
        self.employee_repository = employee_repository

    def handle(self, read_employee_request):
        id = read_employee_request.id
        return self.employee_repository.get_employee_by_id(id)
