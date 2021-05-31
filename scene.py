import abc


class Scene(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def undraw(self):
        pass

    @abc.abstractmethod
    def tick(self):
        pass
