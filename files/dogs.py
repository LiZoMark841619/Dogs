from typing import Any, NamedTuple
from class_tree import instanceTree

class Dog(NamedTuple):
    name: str
    age: int
    color: str
    
    def __call__(self) -> Any:
        return instanceTree(self)

if __name__ == '__main__':
    my_dog = Dog('Killer', 12, 'brown')
    print(my_dog)
    my_dog()
