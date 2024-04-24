from abc import ABC
from abc import abstractmethod
from class_tree import instanceTree

class Animal(ABC):
    num_of_instance = 0
    
    def __init__(self, kind: str, name: str, age: int, color: str) -> None:
        self.kind = kind
        self.name = name
        self.age = age
        self.color = color
        self.count()
    
    def __str__(self):
        return f'{self.__class__.__name__}(name: {self.name}, age: {self.age})'
    
    def __call__(self) -> object:
        return instanceTree(self)
    
    @abstractmethod
    def voice(self):
        return f'{self.kind} does not have voice'
    
    @classmethod
    def count(cls):
        cls.num_of_instance += 1
if __name__ == '__main__': my_animal_1 = Animal('dog', 'LittleOne', 3, 'brown'); print(my_animal_1); print(Animal.num_of_instance)
