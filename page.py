class Page:
    def __init__(self, index, referenced=0):
        self.index = index;
        self.dirty = 0;
        self.referenced = referenced;
        self.age = 0;