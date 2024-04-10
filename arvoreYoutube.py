class TreeNode:
    def __init__(self, data):
        self.data = data
        self.esquerda = None
        self.direita = None


class BinaryTree:
    def __init__(self, data):
        node = TreeNode(data)
        self.raiz = node 

    
        