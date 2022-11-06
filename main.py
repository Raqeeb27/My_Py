class a:
    def __init__(self):
        print("Class A constructor")

    def display(self):
        print("class A display")

class b(a):
    def __init__(self):
        print("Class B constructor")
        super().__init__()

    def display(self):
        print("class B display")


class c(b):
    def __init__(self):
        print("Class C constructor")
        super().__init__()

    def display(self):
        print("class C display")
        super(c,self).display()

a1 = a()
b1 = b()
c1 = c()
c1.display()
