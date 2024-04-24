from animals import Animal
from class_tree import instanceTree

def factory(aklass, *args):
    return aklass(*args)

class Dog(Animal):
    
    def __call__(self) -> object:
        return instanceTree(self)
    
if __name__ == '__main__':
    my_dog = Dog('Killer', 12, 'brown')
    print(my_dog)
    my_dog()
    print(my_dog)
    print(Dog.num_of_instance)
