from garbage import Garbage


class PaperGarbage(Garbage):
    def __init__(self, name, is_squeezed):
        self.name = name
        self.is_squeezed = False
    
    def squeeze(self):
        self.is_squeezed = True