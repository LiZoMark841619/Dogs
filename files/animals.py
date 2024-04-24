from typing import Any, NamedTuple
from class_tree import instanceTree

class Animal(NamedTuple):
    name: str
    age: int
    color: str
    
    def __call__(self) -> object:
        return instanceTree(self)

if __name__ == '__main__':
    my_animal_1, my_animal_2 = Animal('LittleOne', 3, 'brown'), Animal('Biggy', 10, 'white')
    print(my_animal_1)
    my_animal_1()
    