class ParentClass:
    def print_hello(self):
        print('Hello wurl!')

class ChildClass(ParentClass):
    def some_new_method(self):
        print('ParentClass objects don\'t have this method.')

class GrandchildClass(ChildClass):
    def another_new_method(self):
        print('Only GrandchildClass objects have this method.')

print('Create a ParentClass object and call its mwthods.')
parent = ParentClass()
parent.print_hello()

print('Create a ChildClass object and call its methods.')
child = ChildClass()
child.print_hello()
child.some_new_method()

print('Create a GrandChildClass object and call its methods.')
grandchild = GrandchildClass()
grandchild.print_hello()
grandchild.some_new_method()
grandchild.another_new_method()

print('An error:')
parent.some_new_method()