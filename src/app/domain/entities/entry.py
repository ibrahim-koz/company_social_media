from functools import total_ordering
from datetime import datetime


@total_ordering
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

    def __eq__(self, other):
        return self.date == other.date

    def __lt__(self, other):
        date_format = '%Y-%m-%d %H:%M:%S'
        return datetime.strptime(self.date, date_format) < datetime.strptime(other.date, date_format)
