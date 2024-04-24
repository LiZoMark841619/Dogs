def cls_tree(cls_, indent):
    print(cls_, indent * 2)
    for super_cls in cls_.__bases__:
        print(cls_tree(super_cls, indent + 2))
    
def instanceTree(instance):
    return cls_tree(instance.__class__.__name__, 1)