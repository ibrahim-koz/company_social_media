class Entry:
    def __init__(self, id, employee_id, title, content, date):
        self.id = id
        self.employee_id = employee_id
        self.title = title
        self.content = content
        self.date = date

    def change_title(self, title):
        self.title = title

    def change_content(self, content):
        self.content = content