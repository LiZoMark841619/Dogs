from animals import Animal

def factory(aklass, *args):
    return aklass(*args)

class Dog(Animal):
    
    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(self, name, age, color)
        self.kind = 'dog'
        Animal.count()
    
if __name__ == '__main__':
    my_dog = Dog('Killer', 12, 'brown')
    print(my_dog)
    my_dog()
    print(Dog.num_of_instance)
    one, two, three = factory(Dog, 'Killer', 15, 'white'), factory(Dog, 'Tiny', 2, 'black'), factory(Dog, 'Birdy', 2, 'yellow')
    print(one, two, three)
    print(Dog.num_of_instance)
    print(Animal.num_of_instance)
