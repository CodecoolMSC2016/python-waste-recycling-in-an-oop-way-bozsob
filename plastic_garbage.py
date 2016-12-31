from garbage import Garbage


class PlasticGarbage(Garbage):
    def __init__(self, name, is_clean):
        super().__init__(name)
        self.is_clean = False

    def clean(self):
        self.is_clean = True