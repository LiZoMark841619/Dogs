from animals import Animal

def factory(aklass, *args) -> object:
    return aklass(*args)

class Dog(Animal):
    
    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__('dog', name, age, color)
        Animal.count()
        
    def voice(self) -> str:
        return f'{str(self.kind).title()} barks.'