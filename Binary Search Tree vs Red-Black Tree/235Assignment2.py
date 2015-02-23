#CISC 235 Assignment 2. By Scott Killeen, 12sjk11, 10093303
#I confirm that this submission is my own work and
#is consistent with the Queen's regulations on Academic Integrity

#PART 1
import random
#Insert into BST
def insert(tree, value):
    """
    Add value to tree and return pointer to the root of the modified
    tree.  (This will be different from the original root only when
    we're adding the value to an empty tree.)
    """
    if tree == None:
        return {'data':value, 'left':None, 'right':None}
    elif value <= tree['data']:
        tree['left'] = insert(tree['left'],value)
        return tree
    else: # value > tree['data']
        tree['right'] = insert(tree['right'],value)
        return tree


#Search BST
def search(tree,value):
    """
    Searches a tree for a value.  Returns True if value occurs somewhere
    inside tree, False otherwise.
    """
    if tree == None:
        return False
    elif value == tree['data']:
        print value
        return True
    elif value < tree['data']:
        print tree['data']
        return search(tree['left'],value)
    else:
        print tree['data']
        return search(tree['right'],value)

#Get the total Depth (Not Height) of BST
def total_Depth (node, i=0):
    if node == None:
        return 0
    else:
        return i + 1 + total_Depth(node['left'], i+1) + total_Depth(node['right'], i+1)





#PART 2


    

#Inserting into a RBT    
def RB_insert(tree, x):
    tree = rec_RB_insert(tree,x)
    tree['colour'] = 'black'
    return tree 

def has_Red_Child(tree):
    return ((tree['left'])['colour'] == 'red') or ((tree['right'])['colour'] == 'red')

#Inserting into a RBT  
def rec_RB_insert(current,x):
    if current == None or current['leaf'] == True: #leaf
        newNode = {'data':x,'left':None,'right':None, 'colour':'red', 'leaf':False}
        newNode['left'] =  {'data':None,'left':None,'right':None, 'colour':'black', 'leaf':True}
        newNode['right'] = {'data':None,'left':None,'right':None, 'colour':'black', 'leaf':True}
        return newNode
    elif current['data'] < x:
        current['right'] = rec_RB_insert(current['right'],x)
        if current['colour'] == 'red':
            return current
        elif current['right']['colour'] == 'red':
            if has_Red_Child(current['right']):
                return RB_fix_R(current,x)
            else:
                return current
        else:
            return current
    else:
        current['left'] = rec_RB_insert(current['left'],x)
        if current['colour'] == 'red':
            return current
        elif (current['left'])['colour'] == 'red':
            if has_Red_Child(current['left']):
                return RB_fix_L(current,x)
            else:
                return current
        else:
            return current

#Fix Left
def RB_fix_L(current,x):
    sib = current['right']
    child = current['left']
    if sib['colour'] == 'red':
        child['colour'] = 'black'
        sib['colour'] = 'black'
        current['colour'] = 'red'
        return current
    else:
        if x < child['data']:
            grandchild = child['left']
            current['left'] = child['right']
            child['right'] = current
            child['colour'] = 'black'
            current['colour'] = 'red'
            return child
        else:
            grandchild = child['right']
            child['right'] = grandchild['left']
            current['left'] = grandchild['right']
            grandchild['left'] = child
            grandchild['right'] = current
            grandchild['colour'] = 'black'
            current['colour'] = 'red'
            return grandchild

#Fix Right
def RB_fix_R(current,x): 
    sib = current['left']
    child = current['right']
    if sib['colour'] == 'red':
        child['colour'] = 'black'
        sib['colour'] = 'black'
        current['colour'] = 'red'
        return current
    else:
        if x > child['data']:
            grandchild = child['right']
            current['right'] = child['left']
            child['left'] = current
            child['colour'] = 'black'
            current['colour'] = 'red'
            return child
        else:
            grandchild = child['left']
            child['left'] = grandchild['right']
            current['right'] = grandchild['left']
            grandchild['right'] = child
            grandchild['left'] = current
            grandchild['colour'] = 'black'
            current['colour'] = 'red'
            return grandchild

#Search for RBT, shows colour.
def RB_search(tree,value):
    """
    Searches a tree for a value.  Returns True if value occurs somewhere
    inside tree, False otherwise.
    """
    if tree == None:
        return False
    elif value == tree['data']:
        print value,tree['colour']
        return True
    elif value < tree['data']:
        print tree['data'],tree['colour']
        return RB_search(tree['left'],value)
    else:
        print tree['data'],tree['colour']
        return RB_search(tree['right'],value)

#Total depth.
def RBtotal_Depth(tree,i=0):
    if tree == None or tree['leaf'] == True:
        return 0
    else:
        i = i + 1
        return i + RBtotal_Depth(tree['left'],i) + RBtotal_Depth(tree['right'],i)




#part 3
#I used these arrays to help sort out the %s for the table.
smallest = []
smaller = []
small = []
normal = []
big = []
r = 0
k = 500
num = [20,100,500,2500]
for n in num:
    for i in range(1,k):
        sam = random.sample(range(1,n+1), n)
        test = None
        RBtest = None
        for j in sam:
            test = insert(test, j) #insert the values
            RBtest = RB_insert(RBtest, j)
        BSTtotal = total_Depth(test)#get the depths
        RBtotal = RBtotal_Depth(RBtest)
        r = BSTtotal/float(RBtotal)#find the ratio
        if(r<0.5):#adding to arrays for the %s
            smallest.append(r)
        elif(r>=0.50 and r<0.75):
            smaller.append(r)
        elif(r>=0.75 and r<=1.25):
            small.append(r)
        elif(r>1.25 and r<=1.5):
            normal.append(r)
        else:
            big.append(r)

#Used to see the %s
total=len(smallest)+len(smaller)+len(small)+len(normal)+len(big)
print total
print len(smallest)/float(total)
print len(smaller)/float(total)
print len(small)/float(total)
print len(normal)/float(total)
print len(big)/float(total)
