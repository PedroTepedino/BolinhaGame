import abc

from vector import Vector


class Scene(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def undraw(self):
        pass

    @abc.abstractmethod
    def tick(self, mouse_position: Vector, mouse_click_position, elapsed_time: float):
        pass

