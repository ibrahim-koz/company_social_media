from src.app.domain.entities.company import Company


class CompanyFactory:
    def __init__(self, id_generator):
        self.id_generator = id_generator

    def create(self, name):
        return Company(self.id_generator.generate(), name)
