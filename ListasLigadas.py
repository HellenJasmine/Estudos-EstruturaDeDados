class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    
class ListaLigada:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    

    def mostrar(self):
        temp = self.head
        while temp != None:
            print(temp.dado, end=" ")
            temp = temp.next

    def inserir(self, elem):
        node = Node(elem)
        if self.isEmpty():
            self.head = node
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = node 
        self.size += 1

    def inserirIndice(self, elem, indice):
        node = Node(elem)
        if indice == 0:
            node.next = self.head
            self.head = node

        i = 0
        temp = self.head
        while i < indice - 1:
            temp = temp.next
            i += 1
        
        node.next = temp.next
        temp.next = node

    def removerIndice(self, indice):
        #if not self.isEmpty():
            atual = self.head
            i = 0
            while i != indice:
                atual = atual.next
                i += 1
            atual.next = atual.next.next

            self.size -= 1
            
    def removerValor(self, elem):
        atual  = self.head
        while self.isEmpty and atual.data !=  elem:
            anterior = atual
            atual = atual.next
        
        if atual != None and atual.data == elem:
            if atual == self.head:
                self.head = self.head.next
            else:
                anterior.next = atual.next
            self.size -= 1

print("oi")
lista = ListaLigada()
lista.inserir(2)
lista.inserir(5)
lista.inserir(4)
lista.inserir(3)


print("")
lista.removerIndice(1)
lista.mostrar()
            