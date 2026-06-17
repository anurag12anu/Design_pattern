import copy
from abc import ABC, abstractmethod

class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass
    
class Resume(Prototype):
    def __init__(self):
        self.resume=[
            'Summary',
            'skills',
            'projects',
            'Education'
        ]
    def clone(self):
        return copy.deepcopy(self)
    def __str__(self):
        return f"Resume({self.resume})"

default_resume=Resume()
atul_resume=default_resume.clone()
anurag_resume=default_resume.clone()
print(atul_resume)
print(anurag_resume)