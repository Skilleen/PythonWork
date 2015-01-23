"""Bridge Assignment!  NetID: 12sjk11   Student Number: 10093303
    This program will help new bridge players decide what to
    do with their hand!
"""

#This Function will calculate the total high points.
def highCardPoints(hand):
    hpoints = 0
    #Checks for Aces,Kings,Queens,Jacks.
    for index in range(0,len(hand)):
        if hand[index]=="A":
             hpoints+=4
        elif hand[index]=="J":
             hpoints+=1
        elif hand[index]=="Q":
             hpoints+=2
        elif hand[index]=="K":
             hpoints+=3
    return hpoints

#This Function will calculate the total Distribution Points.
def distPoints(hand):
    dpoints = 0
    Dsuitcount=0
    Ssuitcount=0
    Csuitcount=0
    Hsuitcount=0
    #If there is 0 of one suit.
    if "S" not in hand:
         dpoints+=3
    if "C" not in hand:
         dpoints+=3
    if "D" not in hand:
         dpoints+=3
    if "H" not in hand:
         dpoints+=3
    #Checks how many cards of each suit there is.
    for index in range(0,len(hand)):
        if hand[index]=="S":
            Ssuitcount+=1
        elif hand[index]=="D":
            Dsuitcount+=1
        elif hand[index]=="C":
            Csuitcount+=1
        elif hand[index]=="H":
            Hsuitcount+=1
    #If there is only one card of a suit.
    if Dsuitcount==1:
        dpoints+=2
    if Ssuitcount==1:
        dpoints+=2
    if Csuitcount==1:
        dpoints+=2
    if Hsuitcount==1:
        dpoints+=2
    #If there is only two cards of a suit.
    if Dsuitcount==2:
        dpoints+=1
    if Ssuitcount==2:
        dpoints+=1
    if Csuitcount==2:
        dpoints+=1
    if Hsuitcount==2:
        dpoints+=1 
    return dpoints

#Adds the Distpoints and the Highpoints.
def totalPoints(hand):
    total=distPoints(hand)+highCardPoints(hand)
    return total

#This Function will tell the user how to bid.
def bid(hand):
    Dcount=0
    Scount=0
    Ccount=0
    Hcount=0
    if distPoints(hand)+highCardPoints(hand) < 14:
        return "pass"
        #Checks how many cards of each suit there is.
    for index in range(0,len(hand)):
        if hand[index]=="S":
            Scount+=1
        elif hand[index]=="D":
            Dcount+=1
        elif hand[index]=="C":
            Ccount+=1
        elif hand[index]=="H":
            Hcount+=1
    if distPoints(hand) <=1:
        return "1 notrump"
    #If one suit is greater than the other 3
    if Scount > Dcount and Scount > Ccount and Scount> Hcount:
        return "1 spade"
    if Dcount > Scount and Dcount > Ccount and Dcount> Hcount:
        return "1 diamond"
    if Ccount > Scount and Ccount > Dcount and Ccount> Hcount:
        return "1 club"
    if Hcount > Scount and Hcount > Ccount and Hcount> Dcount:
        return "1 heart"
    #If there are suits with the same amount.
    if Hcount == Scount and Scount!=0:
        return "1 spade"
    if  Dcount == Scount and Scount!=0:
        return "1 spade" 
    if Ccount == Scount and Scount!=0:
        return "1 spade"
    if Dcount == Hcount:
        return "1 heart"
    if Ccount == Hcount:
        return "1 heart"
    if Ccount == Dcount:
        return "1 diamond"
            
                       
#Cheers :)                    
