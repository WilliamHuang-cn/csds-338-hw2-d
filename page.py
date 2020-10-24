class Page:
    def __init__(self, index):
        self.index = index;
        self.dirty = 0;
        self.referenced = 0;
        self.age = 0;