class UpdateEntry:
    def __init__(self, entry_repository):
        self.entry_repository = entry_repository

    def handle(self, update_entry_request):
        id = update_entry_request.id
        title = update_entry_request.title
        content = update_entry_request.content
        entry = self.entry_repository.get_entry_by_id(id)
        if title is not None:
            entry.change_title(title)
        if content is not None:
            entry.change_content(content)
        self.entry_repository.update(entry)