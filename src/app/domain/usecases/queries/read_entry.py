class ReadEntry:
    def __init__(self, entry_repository):
        self.entry_repository = entry_repository

    def handle(self, read_entry_request):
        id = read_entry_request.id
        return self.entry_repository.get_entry_by_id(id)