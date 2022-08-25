from datetime import datetime

from src.app.domain.entities.entry import Entry


class EntryFactory:
    def __init__(self, id_generator):
        self.id_generator = id_generator

    def create(self, title, content, employee_id):
        return Entry(self.id_generator.generate(), employee_id, title, content,
                     datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
