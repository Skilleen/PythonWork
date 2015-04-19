#CISC 235 Assignment 4. By Scott Killeen, 12sjk11, 10093303
#I confirm that this submission is my own work and
#is consistent with the Queen's regulations on Academic Integrity
import random
from collections import defaultdict
from heapq import *


#Random Graph
def randomGraph(n):
    S = [1]
    edges = []
    checker = []
    for  i in range(2,n):
        x = random.randint(1,i-1)
        S.append(random.randint(1,i-1))
        for s in S:
             w = random.randint(10,100)
             check = (str(i), str(s))
             if check not in checker: # Checking to see if edge already existed or not
                checker.append(check)
                edge = (str(i),str(s),w)
                edges.append(edge)
    return edges # return list of edges




#PART1 Breadth-First Search
def BFS(lis, v):
    Q = [] #create an empty queue Q
    first = v
    path = []  #The Path taken
    newLis = []
    visited = [] #To store which vertices have been marked
    totalW = 0 #Total Wieght
    Q.append([first]) #append v to Q
    visited.append(first)  #mark v "visited"
    current = first
    for x in lis:
        newLis.append((x[1],x[0],x[2]))  #Add the edges to newLis
    lis.extend(newLis)
    lis.sort()
    for t in lis:
        if t[0]==v: #Find the start vertex
            path.append(t) #append it to the path
    for c in path:
        if c[1] not in visited: #If not marked
            visited.append(c[1])
            Q.append(c[1]) #add to the que.
            totalW += c[2]
    Q.pop(0) #Remove from Que
    current = Q[0] #New current
    while Q: #While Q is not empty
        for s in lis:
            if s[0] == current:
                path.append(s) #add to path
        for n in path:
            if n[1] not in visited:
                visited.append(n[1]) #mark as visited
                Q.append(n[1]) #add to que
                totalW +=n[2] #add the edges weight
        Q.pop(0)
        if len(Q) != 0:
            current = Q[0]
        else:
            return totalW #Once all have been visited.




#PART 2, Prims Alg.
def prim( vertex, edges ):
    totalW = 0 #total weight
    connect = defaultdict( list ) #connections
    for v1,v2,c in edges: 
        connect[ v1 ].append( (c, v1, v2) ) 
        connect[ v2 ].append( (c, v2, v1) ) #Add each edge (and it's reverse)
    mst = [] #the tree
    visited = []
    visited.append(vertex)#list of visited vertices
    usable_edges = connect[ vertex ][:]
    heapify( usable_edges )
 
    while usable_edges: #While there are still edges to be used
        cost, v1, v2 = heappop( usable_edges )
        if v2 not in visited: #If not in VA
            visited.append( v2 ) #add to VA
            mst.append( ( v1, v2, cost ) )
            for e in connect[ v2 ]:
                if e[ 2 ] not in visited:
                    heappush( usable_edges, e )
    for i in mst:  #Print the tree and get the total weight.
        totalW+=i[2]
    return totalW






#PART 1 and 2 Test
#Given graph
edges = [ ("1", "2", 15), ("1", "4", 7),
          ("1","5",10), ("2", "3", 9), ("2", "4", 11),
      ("2", "6", 9),
      ("3", "5", 12), ("3", "6", 7),
      ("4", "5", 8), ("4", "6", 14),
      ("5", "6", 8)]
print "PART 1 and 2 weights\n"
vertex = random.randint(1,6)
vertex = str(vertex)
print "prim:", prim(vertex, edges )
print "BFS:", BFS(edges,vertex)
print "\n"


#PART 3 expierment
ns = [100,200,300,400,500]
print "PART 3\n"
for n in ns:
    print "Ratio for: ",n
    count=0.0;
    for i in range(10):
        g = randomGraph(n)
        randomVertex = random.randint(1,n-1)
        randomVertex = str(randomVertex)
        bfs = BFS(g,randomVertex)
        bfs = float(int(bfs))
        prims = prim(randomVertex,g)
        prims = float(int(prims))
        ratio = prims/bfs
        count+=ratio
    averageratio = count/10.0
    print averageratio


