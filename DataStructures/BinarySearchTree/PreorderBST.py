'''
Create a Binary Search Tree from list A containing N elements. Insert elements in the same order as given. Print the pre-order traversal of the subtree with root node data equal to Q (inclusive of Q), separating each element by a space.

Input:
First line contains a single integer N – number of elements.
Second line contains N space-separated integers. 
Third line contains a single integer Q – the element whose subtree is to be printed in pre-order form.

Output:
Print K space-separated integers – where K is the number of elements in the subtree of Q (inclusive of Q)

Constraints:



SAMPLE INPUT 
4
2 1 3 4
3
SAMPLE OUTPUT 
3
4

'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def insert(root, node):
    if root is None:
        root = node
        
    if node.data < root.data:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)

def preorder(QNode):
    if(QNode is not None):
        print(QNode.data)
        preorder(QNode.left)
        preorder(QNode.right)

def search(root, Q):
    if root is None or Q == root.data:
        preorder(root)
        return
    if Q < root.data:
        search(root.left,Q)
    else:
        search(root.right,Q)

if __name__ == "__main__":
    N = int(input())
    elements = input().split()
    root = Node(int(elements[0]))
    for x in elements[1:]:
        insert(root,Node(int(x)))
    Q = int(input())
    search(root,Q)