class Stack:
    def __init__(self):
        self.elements = []
    def push(self,item):
        self.elements.append(item)
        print(self.elements)
    def popit(self):
        self.elements.pop()
        print(self.elements)
    def is_empty(self):
        if not self.elements:
            return print("Stack is Empty")
        else:
            return print(self.elements)
    def show(self):
        print(self.elements)

    def size(self):
        return print(len(self.elements))

stack = Stack()
stack.push(5)
stack.push(6)
stack.is_empty()
stack.push(7)
stack.show()
stack.size()
stack.popit()
stack.show()
stack.popit()
stack.show()
stack.popit()
stack.is_empty()
stack.size()