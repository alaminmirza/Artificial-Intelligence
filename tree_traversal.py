class Tree:
    def __init__(self, data = None, left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

A = Tree('A')
B = Tree('B')
C = Tree('C')
D = Tree('D')
E = Tree('E')
F = Tree('F')
G = Tree('G')
H = Tree('H')
I = Tree('I')

A.left_child = B
A.right_child = C

B.left_child = D
B.right_child = E

C.left_child = F
C.right_child = G

G.left_child = H
G.right_child = I

def in_order(tree):
    if tree:
        in_order(tree.left_child)
        print (tree.data)
        in_order(tree.right_child)

def pre_order(tree):

    if tree:
        print(tree.data)
        pre_order(tree.left_child)
        pre_order(tree.right_child)

def post_order(tree):

    if tree:
       post_order(tree.left_child)
       post_order(tree.right_child)
       print(tree.data)

print("\nIn Order: ")
in_order(A)
print("\nPre Order: ")
pre_order(A)
print("\nPost Order: ")
post_order(A)