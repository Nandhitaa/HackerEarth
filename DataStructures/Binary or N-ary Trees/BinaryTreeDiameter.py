'''
Given a binary tree which has T nodes, you need to find the diameter of that binary tree. The diameter of a tree is the number of nodes on the longest path between two leaves in the tree.

Input:
First line contains two integers, T and X, number of nodes in the tree and value of the root.
Next  lines contain details of nodes.
Each detail of node contains two lines. First lines contains a string and second line contains an integer, which denotes the path of the node and the value of the node respectively.

String consists of only L or R. L denotes left child and R denotes right child. ( Look at the sample explanation for more details )

Output:
Print the diameter of the binary tree.

Constraints:


SAMPLE INPUT 
5 1
L
2
R
3
LL
4
LR
5
SAMPLE OUTPUT 
4

'''

class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    
    return max(height(node.left), height(node.right)) + 1
    
def diameter(root):
    if root is None:
        return 0
    
    lheight = height(root.left)
    rheight = height(root.right)
    
    ldiameter = diameter(root.left) 
    rdiameter = diameter(root.right) 
    
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

def insert(node, position, location, data, end):
    if location[position] == 'L':
        if node.left is None:
            node.left = Node()
        currNode = node.left
    elif location[position] == 'R':
        if node.right is None:
            node.right = Node()
        currNode = node.right
    
    if position == end:
        currNode.data = data
        return

    if position < end:
        insert(currNode, position + 1, location, data, end)

if __name__ == '__main__':
    start = input()
    N = int(start.split()[0])
    root = Node(start.split()[1])
    for i in range(N-1):
        location = input()
        data = int(input())
        end = len(location) - 1
        insert(root, 0, location, data, end)
    print(diameter(root))