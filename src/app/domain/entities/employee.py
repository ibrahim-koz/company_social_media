class Employee:
    def __init__(self, id, name, salary, company_id, entries=None):
        if entries is None:
            entries = set()
        self.id = id
        self.name = name
        self.salary = salary
        self.company_id = company_id
        self.entries = entries

    def add_entry(self, entry_id):
        self.entries.add(entry_id)

    def has_entry(self, entry_id):
        return entry_id in self.entries

    def remove_entry(self, entry_id):
        self.entries.remove(entry_id)

    def change_name(self, name):
        self.name = name

    def change_salary(self, salary):
        self.salary = salary

    def change_company_id(self, company_id):
        self.company_id = company_id