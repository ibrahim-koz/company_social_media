from src.app.domain.exceptions.entry_not_found_exception import EntryNotFoundException
from src.app.domain.repositories.entry_repository import EntryRepository


class MockEntryRepository(EntryRepository):
    def __init__(self):
        self.entries = {}

    def add(self, entry):
        self.entries[entry.id] = entry

    def get_entry_by_id(self, id):
        try:
            return self.entries[id]
        except KeyError:
            raise EntryNotFoundException()

    def filter(self, function):
        return list(filter(function, self.entries.values()))

    def update(self, entry):
        self.entries[entry.id] = entry

    def remove(self, id):
        try:
            del self.entries[id]
        except KeyError:
            raise EntryNotFoundException()
