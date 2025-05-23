from abc import ABC, abstractmethod

class DataLoader(ABC):

    @abstractmethod
    def load(self,path_to_folder:str):
        pass