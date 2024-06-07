from abc import ABC, abstractmethod

class DataLoader(ABC):
    @abstractmethod
    def load_data(self):
        pass



