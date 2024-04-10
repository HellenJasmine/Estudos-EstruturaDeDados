'''class Node:
    def __init__(self, dado):
        self.dado = dado
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1

    def lenght(self):
        return self._size
    
    def isEmpty(self):
        if self._size == 0:
            return False

if __name__ == "__main__":
    pilha = Stack()
    
    pilha.push(5)
    pilha.push(10)
 
    print(pilha.top.dado)'''


class No:
    def __init__(self, dado):
        self.dado = dado
        self.next = None 


class Stack:
    def __init__(self):
        self.top = None 
        self.size = 0

    def push(self, elem):
        node = No(elem)
        node.next = self.top
        self.top = node
        self.size += 1 

    def len(self):
        return self.size

    def isEmpty(self):
        return self.top is None
    
    def peek(self):
        if not self.isEmpty():
            return self.top.dado
        
    def pop(self):
        if not self.isEmpty():
            node = self.top
            self.top = self.top.next
            self.size -= 1
            return node.dado

if __name__ == "__main__":
    pilha = Stack()
    pilha.push(5)

    print(pilha.peek())
    pilha.pop()
    print(pilha.isEmpty())



    