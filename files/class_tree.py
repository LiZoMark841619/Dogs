def cls_tree(cls, indent):
    print(indent * '-', cls.__name__)
    for super_cls in cls.__bases__:
        cls_tree(super_cls, indent + 2)
    
def instanceTree(instance):
    print(f'Classtre of object {instance.__dict__}: ')
    cls_tree(instance.__class__, 1)