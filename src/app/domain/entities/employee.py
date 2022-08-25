class Employee:
    def __init__(self, id, name, salary, company_id, entries=None):
        if entries is None:
            entries = []
        self.id = id
        self.name = name
        self.salary = salary
        self.company_id = company_id
        self.entries = entries

    def add_entry(self, entry_id):
        self.entries.append(entry_id)

    def has_entry(self, entry_id):
        try:
            self.entries.index(entry_id)
            return True
        except ValueError:
            return False
