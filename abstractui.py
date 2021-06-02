import abc

from vector import Vector


class AbstractUi(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def show(self):
        pass

    @abc.abstractmethod
    def hide(self):
        pass

    @abc.abstractmethod
    def update(self, mouse_position: Vector, mouse_click_position):
        pass
