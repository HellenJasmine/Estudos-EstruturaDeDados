class No:
    def __init__(self, data):
        self.data = data
        self.next = None 

class ListaLigada:
    def __init__(self):
        self.head = None
        self.size = 0

    def estaVazia(self):
        return self.head is None 
    
    def lenght(self):
        return self.size
    
    
    def inserir(self, elem, index = None):
        node = No(elem)
        if self.estaVazia() or index == None:
            node.next = self.head
            self.head = node 

        elif index == self.size:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
        
        else:
            temp = self.head
            i = 0
            while i < index -1:
                temp = temp.next
                i += 1
            node.next = temp.next
            temp.next = node
        self.size += 1

    def removerValor(self, valor):
        atual = self.head
        ante = None 
       
        while atual != None and atual.data != valor:
            ante = atual
            atual = atual.next
        if atual != None :
           if atual == self.head:
            self.head = self.head.next
           else:
            ante.next = atual.next
        self.size -= 1

    def removerIndice(self, indice):
        temp = self.head
        i = 0
        if indice == 0:
            self.head = self.head.next
        while temp.next != None and i < indice - 1:
            temp = temp.next
            i += 1
        temp.next = temp.next.next
        
        self.size -= 1

        
    def mostrar(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
            

    def buscar(self, valor):
        temp = self.head
        while temp != None and temp.data != valor:
            temp = temp.next
        if temp != None:
            return temp
        return None
    


lista = ListaLigada()
lista.inserir(4)
lista.inserir(6)
lista.inserir(2)
lista.inserir(7)
lista.inserir(1)
lista.inserir(3)
print(lista.head.data)
lista.mostrar()


            

        
        