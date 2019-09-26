# Abstract Basic scene
class BasicScene(object):
    def __init__(self, name):
        self.__name = name

    def load(self):
        pass

    def update(self, deltaTime):
        pass

    def display(self, screen):
        pass

    def getName(self):
        return self.__name
