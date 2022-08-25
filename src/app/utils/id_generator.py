class IdGenerator:
    def __init__(self):
        self.id = 0

    def generate(self):
        self.id += 1
        return self.id
