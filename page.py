class Page:
    def __init__(self, index, referenced=0):
        self.index = index;
        self.dirty = 0;
        self.referenced = referenced;
        self.age = 0;

    def __str__(self):
        return str(self.index);
    
    def __repr__(self):
        return 'Page with index '+str(self.index);