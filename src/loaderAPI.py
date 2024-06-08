from abc import ABC, abstractmethod

class DataLoader(ABC):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @abstractmethod
    def load_data(self):
        pass



