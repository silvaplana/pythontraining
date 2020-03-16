from abc import ABC, abstractmethod


class ModelEvent(ABC):
    def __init__(self):
        pass



    @abstractmethod
    def onMacsHierarchyUpdated(self, value):
        pass

    @abstractmethod
    def onSicsHierarchyUpdated(self, value):
        pass

    @abstractmethod
    def onSourceDestUpdated(self, value):
        pass

    def onInfoLabelUpdate(self, value):
        pass