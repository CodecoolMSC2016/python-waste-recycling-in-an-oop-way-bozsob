from garbage import Garbage


class PaperGarbage(Garbage):
    def __init__(self, name, is_squeezed = None):
        super().__init__(name)
        self.is_squeezed = is_squeezed
    
    def squeeze(self):
        if self.is_squeezed == False:
            self.is_squeezed = True