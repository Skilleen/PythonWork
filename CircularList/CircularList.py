"""CircularList Assignment  NetID: 12sjk11   Student Number: 10093303
    
"""

#Function used to help turn the python list into a link list.
def liststring(lis):
    listy = "["
    isFirst=True
    node=lis
    if lis==None:
        return "[]"
    node=node['next']
    
    while node!=lis:
        if isFirst:
            isFirst=False
        else:
            listy += ","
        listy += str(node['data'])
        node= node['next']
    if node!=node['next']:
        listy+=","
    listy+=node['data']
    listy+="]"
    return listy
#Prints the list.
def printList(lis):
    print liststring(lis)

#Adds a value into the linked list.
def add(circList, newValue):
    node=circList
    if circList==None:
        node1={'data':newValue}
        node1['next']=node1
        return node1
    else:
        node2={'data':newValue}
        node2['next']=node['next']
        node['next']=node2
        return circList

#Returns the current value of the list.
def current(circList):
    node=circList
    if circList==None:
        return None
    else:
        node=node['next']
        cur=node['data']
        return cur
    
#Advances the current node in the list.
def advance(circList):
    node=circList
    if circList==None:
        return None
    else:
        node2=node['next']
        return node2
    
#Returns the size of the list.   
def count(circList):
    if circList==None:
        return 0
    count = 1
    node = circList
    node=node['next']
    while node!=circList:
        count+=1
        node=node['next']
    return count

#Searchs for a value in the list.
def search(circList, value):
    node=circList
    if circList == None:
        return None
    if node['data']==value:
            return True
    node=node['next']
    while node!=circList:
        if node['data']==value:
            return True
        else:
            node=node['next']
    return False

#Deletes the current node in the linked list.
def delete(circList):
    if circList == None:
        return None
    node=circList
    node=node['next']
    nodetodel=circList
    #if there is only one value
    if nodetodel==nodetodel['next']:
        nodetodel=None
        return nodetodel
    #delete the current value.
    nodetodel['next']=node['next']
    return nodetodel
    
        
