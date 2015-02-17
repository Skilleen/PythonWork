#CISC 235 Assignment 1. By Scott Killeen, 12sjk11, 10093303
#I confirm that this submission is my own work and
#is consistent with the Queen's regulations on Academic Integrity

import random
import time



def bin_search(A,first,last,target):
    # returns index of target in A, if present
    # returns -1 if target is not present in A
    if first > last:
        return -1
    else:
        mid = (first+last)/2
    if A[mid] == target:
        return mid
    elif A[mid] > target:
        return bin_search(A,first,mid-1,target)
    else:
        return bin_search(A,mid+1,last,target)


            

def trin_search(A,first,last,target):
    # returns index of target in A, if present
    # returns -1 if target is not present in A
    if first > last:
        return -1
    else:
        one_third = first + (last-first)/3
        two_thirds = first + 2*(last-first)/3
        if A[one_third] == target:
            return one_third
        elif A[one_third] > target:
        # search the left-hand third
            return trin_search(A,first,one_third-1,target)
        elif A[two_thirds] == target:
            return two_thirds
        elif A[two_thirds] > target:
        # search the middle third
            return trin_search(A,one_third+1,two_thirds-1,target)
        else:
        # search the right-hand third
            return trin_search(A,two_thirds+1,last,target)


#Function For using the Binary Search    
def binaryTime(lis, n):
    from random import randint
    timeStart = 0
    timeEnd = 0
    newLis = []
    value = n/5
    for i in range(value):
        index = randint(0,len(lis)-1)
        newLis.append(lis[index])
    timeStart = time.clock()
    for j in range(len(newLis)-1):
        bin_search(lis, 0, len(lis), newLis[j])
    timeStop = time.clock()
    totalTime = timeStop - timeStart
    print "Binary Search Time: ", totalTime

#Function for using the Trinary Search
def trinaryTime(lis, n):
    from random import randint
    timeStart = 0
    timeEnd = 0
    newLis = []
    value = n/2
    for i in range(value):
        index = randint(0,len(lis)-1)
        newLis.append(lis[index])
    timeStart = time.clock()
    for j in range(len(newLis)-1):
        trin_search(lis, 0, len(lis), newLis[j])
    timeStop = time.clock()
    totalTime = timeStop - timeStart
    print "Trinary Search Time: ", totalTime, "\n"

#For the Second Exp
def secondExp(n):
    lis = random.sample(range(n*2), n)
    lis.sort()
    k = random.sample(range((n*2)+1, n*4), n/2)
    binStart = time.clock()
    for x in range(len(k)-1):
        bSearch = bin_search(lis,0,len(lis)-1,k[x])
    binEnd = time.clock()
    binTime = binEnd - binStart
    print "When n is:", n, "\n"
    print "Binary Search Time: ", binTime

    triStart = time.clock()
    for y in range(len(k)-1):
        tSearch = trin_search(lis,0,len(lis)-1,k[x])
    triEnd = time.clock()
    triTime = triEnd - triStart
    print "Trinary Search Time:", triTime, "\n"
      
#Generating a random list.
def randomizer(lis, length):
    for i in range(length):
        lis.append(random.randint(0, length))
        

#Creating lists and values  
n = [10000, 25000, 50000, 100000, 500000]

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

#Calling Functions and printing out data.
print "EXP 1 \n"
randomizer(list1, n[0])
list1.sort()
print "When n is: ", n[0], "\n"
binaryTime(list1, n[0])
trinaryTime(list1, n[0])

randomizer(list2, n[1])
list2.sort()
print "When n is: ", n[1], "\n"
binaryTime(list2, n[1])
trinaryTime(list2, n[1])

randomizer(list3, n[2])
list3.sort()
print "When n is: ", n[2], "\n"
binaryTime(list3, n[2])
trinaryTime(list3, n[2])

randomizer(list4, n[3])
list4.sort()
print "When n is: ", n[3], "\n"
binaryTime(list4, n[3])
trinaryTime(list4, n[3])

randomizer(list5, n[4])
list5.sort()
print "When n is: ", n[4], "\n"
binaryTime(list5, n[4])
trinaryTime(list5, n[4])

print "EXP 2 \n"
secondExp(10000)
secondExp(25000)
secondExp(50000)
secondExp(100000)
secondExp(500000)



