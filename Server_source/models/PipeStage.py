from abc import ABC, abstractmethod

class PipeStage(ABC):

    @abstractmethod
    def flow(self,path_to_input_folder:str):
        pass