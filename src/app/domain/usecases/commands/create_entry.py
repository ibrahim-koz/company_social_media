class CreateEntry:
    def __init__(self, entry_repository, entry_factory, employee_repository):
        self.entry_factory = entry_factory
        self.entry_repository = entry_repository
        self.employee_repository = employee_repository

    def handle(self, create_entry_request):
        title = create_entry_request.title
        content = create_entry_request.content
        employee_id = create_entry_request.employee_id

        new_entry = self.entry_factory.create(title, content, employee_id)
        self.entry_repository.add(new_entry)

        employee = self.employee_repository.get_employee_by_id(employee_id)
        employee.add_entry(new_entry.id)
        self.employee_repository.update(employee)
