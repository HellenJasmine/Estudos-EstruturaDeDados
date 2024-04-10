class Stack:
    def __init__(self):
        self.itens = list()
    
    def push(self, item):
        self.itens.append(item)

    def isEmpty(self):
        return len(self.itens) == 0

    def peek(self):
        if not self.isEmpty():
            return self.itens[-1]
    
    def len(self):
        return len(self.itens)
    
    def pop(self):
        if not self.isEmpty():
            return self.itens.pop
