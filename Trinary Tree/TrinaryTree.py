"""
Starting code for Assignment 5.  Functions to create, view and modify
"trinary trees".

12sjk11, 10093303

Fill in the bodies of the empty functions below and subtitute your
student number(s) or netId(s) for my name above.
"""

def printTree(tree, indent=0):
    """
    Prints an indented representation of a trinary tree.  The second
    parameter determines how far the tree is to be indented from the
    left margin.  Just like the indented representation of binary trees,
    this representation looks like a drawing of a tree without the
    connecting lines if you tilt your head to the left.

    STUDENTS MUST NOT CHANGE THIS FUNCTION!  That means the rest of your
    code has to use the representation used here.
    """
    if tree == None:
        return # don't print anything
    elif tree['data2'] == None: # one data element, no children
        print " "*indent + str(tree['data1'])
    else: # two data elements, may have up to three children
        printTree(tree['right'],indent+4)
        print " "*indent + str(tree['data2'])
        printTree(tree['middle'],indent+4)
        print " "*indent + str(tree['data1'])
        printTree(tree['left'],indent+4)

def add(tree, newValue):
    """
    Adds newValue to tree and returns a pointer to the root of the
    modified tree.  If newValue is already in the tree, doesn't change
    the tree (but this is not an error).
    """
    if tree == None: 
        return {'data1':newValue, 'data2':None, 'middle':None, 'left':None, 'right':None}
    if newValue > tree['data1'] and tree['data2']==None:
        tree['data2']=newValue
        return tree
    elif newValue < tree['data1'] and tree['data2']==None:
        tree['data2']=tree['data1']
        tree['data1']=newValue
        return tree
    if newValue < tree['data1']:
        tree['left'] = add(tree['left'],newValue)
        return tree
    elif newValue > tree['data1'] and tree['data2'] > newValue:
        tree['middle']=add(tree['middle'],newValue)
        return tree
    else: # newValue > tree['data2']
        tree['right'] = add(tree['right'],newValue)
        return tree


       

def treeFromList(values):
    """
    Parameter must be a Python lists of values.  Returns a tree
    created by adding each value from the list to the tree, in order.
    A convenience function for testing.
    """
    tree = None
    for v in values:
        tree = add(tree,v)
    return tree

import random
def randomTree(numNodes):
    """
    Creates a tree with the specified number of nodes using random numbers.
    A helper to generate trees for testing.  The tree may actually have fewer
    nodes than the requested number if randInt happens to come up with
    duplicates of the same number.
    """
    tree = None
    for i in range(numNodes):
        tree = add(tree, random.randint(1,100))
    return tree
    

def search(tree,value):
    """
    Searches a tree for a value.  Returns True if value occurs somewhere
    inside tree, False otherwise.
    """
    if tree == None:
        return False
    elif value == tree['data1'] or value == tree['data2']:
        return True
    elif value < tree['data1']:
        return search(tree['left'],value)
    elif value > tree['data1'] and value < tree['data2']:
        return search(tree['middle'],value)
    else: # value > tree['data2']:
        return search(tree['right'],value)

def total(tree):
    """
    Returns the total of all the numbers in a tree.  If the tree is empty,
    the total is zero.
    """
    if tree == None:
        return 0
    else:
        leftCount = total(tree['left'])
        rightCount = total(tree['right'])
        middleCount = total(tree['middle'])
        if tree['data2']!=None:
            totals = tree['data1']+tree['data2']
        else:
            totals=tree['data1']

        return totals+leftCount+rightCount+middleCount
            
        


def height(tree):
    """
    Returns the height of the tree -- the length of the longest path from
    the root to a leaf.
    """
    if tree == None:
        return 0
    else:
        leftHeight = height(tree['left'])
        rightHeight = height(tree['right'])
        middleHeight = height(tree['middle'])
        return max(leftHeight,middleHeight,rightHeight)+1

def findMin(tree):
    """
    Returns the smallest value in the tree, or None if the tree is empty.
    """
    if tree['left']==None:
        return tree['data1']
    else:
        return findMin(tree['left'])


def deleteMin(tree):
    """
    Deletes the smallest value in the tree and returns the modified tree.
    No effect if the tree is empty.
    """
    if tree['left']==None:
       tree['data']=None
    else:
        return findMin(tree['data'])
    
    

def treeToList(tree):
    """
    Returns a list of all the values in the tree, in ascending order
    """
    if tree == None:
        return []
    else:
        left = treeToList(tree['left'])
        right = treeToList(tree['right'])
        middle = treeToList(tree['middle'])
        if tree['data2']!=None:
            one=[tree['data1']]
            two=[tree['data2']]
        else:
            one=[tree['data1']]
            two=[]

        return left+one+middle+two+right

