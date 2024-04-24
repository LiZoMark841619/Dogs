from animals import Animal

class Dog(Animal):
    pass
    
if __name__ == '__main__':
    my_dog = Dog('Killer', 12, 'brown')
    print(my_dog)
    my_dog()
    print(my_dog)
