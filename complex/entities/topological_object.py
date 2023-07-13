from abc import ABC, abstractmethod


class TopologicalObject(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def write(self):
        pass
