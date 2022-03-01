"""
Write a code that prints out individual scores of two players in a game of cricket 
where score is given as runs per ball in an array. In a game of cricket a person changes 
strike if he scores an odd number, and keeps strike with him if he scores an even number. 
No need to consider changing strike after every 6 balls or an over.

    Sample Input1: [1,2]
    Output1: p1: 1, p2: 2
    
    Sample Input2: [1,2,3,2,1]
    Output2: p1: 4, p2: 5
"""

lis = [1,2,3,2,1,2,5,9,8,9]

#initialise scores to zero
p1 = 0
p2 = 0

#to keep track of strike
track = 0

for i in lis:
    if(i%2!=0):   # checking odd number
        if(track==0):
            p1 = p1+i
            track = 1
        else:
            p2 = p2+i
            track = 0 
    else:
        if(track == 1):
            p2 = p2 + i
        else:
            p1 = p1+i
 
print("Player1 scores " + str(p1))
print("Player2 scores " + str(p2))    

#method - 2 : get P1 score and subtracts it from sum of input list to get P2 score
#print("Player2 scores " + str(sum(lis)-p1)) 
