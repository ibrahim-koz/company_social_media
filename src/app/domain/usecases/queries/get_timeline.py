class GetTimeline:
    def __init__(self, employee_repository, entry_repository):
        self.employee_repository = employee_repository
        self.entry_repository = entry_repository

    def handle(self, get_timeline_request):
        employee_id = get_timeline_request.employee_id
        employee = self.employee_repository.get_employee_by_id(employee_id)
        entries = sorted([self.entry_repository.get_entry_by_id(entry_id) for entry_id in employee.entries])
        return entries
