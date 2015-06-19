class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import random
data = [ 2, 4, 6, 7, 5, 1, 9, 0 ]

print data


root = TreeNode(data[0])
def add_node(node, x):
    newnode = TreeNode(x)
    if x > node.val:
        if node.right:
            add_node(node.right, x)
        else:
            node.right = newnode
    else:
        if node.left:
            add_node(node.left, x)
        else:
            node.left = newnode


def display_tree(node):
    level = 0
    while node.right or node.left:
    # print "left of %s" % node.val
    traverse_tree(node.left, level=level+1)
    # print "right of %s" % node.val
    traverse_tree(node.right, level=level+1)


def reverse_tree(node):
    if node.right or node.left:
        tmp = node.left
        node.left = node.right
        node.right = tmp
        if node.right:
            reverse_tree(node.right)
        if node.left:
            reverse_tree(node.left)


for x in data[1:]:
    add_node(root, x)

traverse_tree(root)    

print "------------reverse tree------------"

reverse_tree(root)
traverse_tree(root)    
