from animals import Animal
from dogs import Dog, factory


one, two, three = factory(Dog, 'Killer', 15, 'white'), factory(Dog, 'Tiny', 2, 'black'), factory(Dog, 'Birdy', 2, 'yellow')
print(one, two, three)
print(Dog.num_of_instance)
print(Animal.num_of_instance)

my_dog = Dog('Killer', 12, 'brown')
print(my_dog)
my_dog()

# my_animal_1 = Animal('dog', 'LittleOne', 3, 'brown')
# print(my_animal_1)