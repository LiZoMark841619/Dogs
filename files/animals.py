from abc import ABC
from abc import abstractmethod

class Animal(ABC):
    num_of_instance = 0
    
    def __init__(self, name: str, age: int, color: str) -> None:
        self.name = name
        self.age = age
        self.color = color
        self.count()
    
    def __str__(self):
        return f'{self.__class__.__name__}(name: {self.name}, age: {self.age}, color: {self.color})'
    
    @classmethod
    def count(cls):
        cls.num_of_instance += 1
        
    
if __name__ == '__main__':
    my_animal_1 = Animal('LittleOne', 3, 'brown')
    print(my_animal_1)
    print(Animal.num_of_instance)