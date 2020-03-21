from abc import ABC, abstractmethod


class ModelEvent(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def onValueUpdated(self, key, value):
        pass

    def onInfoLabelUpdate(self, value):
        pass