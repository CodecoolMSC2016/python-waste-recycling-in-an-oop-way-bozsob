from garbage import Garbage


class PlasticGarbage(Garbage):
    def __init__(self, name, is_clean = None):
        super().__init__(name)
        self.is_clean = is_clean

    def clean(self):
        if self.is_clean == False:
            self.is_clean = True