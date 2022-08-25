class DeleteEntry:
    def __init__(self, employee_repository, entry_repository):
        self.employee_repository = employee_repository
        self.entry_repository = entry_repository

    def handle(self, delete_entry_request):
        id = delete_entry_request.id
        entry = self.entry_repository.get_entry_by_id(id)
        employee = self.employee_repository.get_employee_by_id(entry.employee_id)
        self.entry_repository.remove(id)
        employee.remove_entry(id)
        self.employee_repository.update(employee)
