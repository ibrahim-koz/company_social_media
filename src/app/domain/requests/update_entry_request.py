class UpdateEntryRequest:
    def __init__(self, id, title=None, content=None):
        self.id = id
        self.title = title
        self.content = content
