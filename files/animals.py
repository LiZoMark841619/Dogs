from abc import ABC, abstractmethod

def cls_tree(cls, indent):
    print(indent * '-', cls.__name__)
    for super_cls in cls.__bases__:
        cls_tree(super_cls, indent + 2)

def instanceTree(instance):
    print(f'Classtre of object {instance.__dict__}: ')
    cls_tree(instance.__class__, 1)
    
class Animal(ABC):
    num_of_instance = 0
    
    def __init__(self, kind: str, name: str, age: int, color: str) -> None:
        self.kind = kind
        self.name = name
        self.age = age
        self.color = color
        self.count()
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}(name: {self.name}, age: {self.age})'
    
    def __call__(self) -> object:
        return instanceTree(self)
    
    @abstractmethod
    def voice(self) -> str:
        return f'{self.kind} does not have voice'
    
    @classmethod
    def count(cls):
        cls.num_of_instance += 1