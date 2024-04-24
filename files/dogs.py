from typing import NamedTuple
from class_tree import instanceTree

class Dog(NamedTuple):
    name: str
    age: int
    color: str

if __name__ == '__main':
    my_dog = Dog('Killer', 12, 'brown')
    print(my_dog)
