"""A program to play the changeling game. Enter 2 words and a max amount of
    steps, if the program can form the second word in those steps, it will
    return the path it took.    
"""
import string
import WordLookup

#Helper function.
def oneLetterDiff(word):
    WordLookup.lookup(word)
    lis=[]
    for i in range (0,len(word)):
        for j in range(0,len(string.ascii_lowercase)):
            words=string.ascii_lowercase[j]
            if i==0:
                newword=words+word[1:]
                if newword in WordLookup.wordList:
                    if newword != word:
                        lis.append(newword)
            else:
                newword=word[:i]+words+word[i+1:]
                if newword in WordLookup.wordList:
                    if newword != word:
                        lis.append(newword)        
    return lis


def changeling(word,goal,steps):
    if steps<1:
        if word==goal and steps > -1:
            return [goal]
        return None
    if len(word) != len(goal):
        return None
    if word not in WordLookup.wordList or goal not in WordLookup.wordList:
        return None
    if steps>=0:
        if word==goal:
            return [goal]
        else:
            #temp list to store the simalar words.
            templis=[]
            templis=oneLetterDiff(word) 
            
            for i in templis:
                x  = changeling(i,goal,steps-1)
                if x == None:
                    pass
                else:
                    return [word]+x
                








                
            
        
        
