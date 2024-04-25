from animals import Animal

def factory(aklass, *args):
    return aklass(*args)

class Dog(Animal):
    
    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(self, name, age, color)
        self.kind = 'dog'
        Animal.count()
        
    def voice(self):
        return f'{str(self.kind).title()} barks.'