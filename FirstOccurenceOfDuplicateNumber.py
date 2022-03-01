#Write a code that prints out the first occurrence of a duplicate in a given array of integers
#   Sample Input: [1,2,3,2,1]
#    Output: 2

lis = [1,2,3,2,1]
unique_nums = []

#initialise to zero if duplicate number is not present
first_occurence = 0

#to keep track if duplicate number found or not
track = 0

#traversing list to find first duplicate number
for i in lis:
    if i in unique_nums:
        first_duplicate = i
        track = 1
        break
    else:
        unique_nums.append(i)

if(track==1):
    
    #method - 1 :- by using index() function
    print(lis.index(first_duplicate)+1)
    
    #method - 2 :- compare first_duplicate number with each element in given list and return first occurrence
    """
    for j in range(len(lis)):
        if(lis[j]==first_duplicate):
            first_occurence = j+1
            break
    print(first_occurence) """
    
else:
    #return 0 if duplicate number not present
    print(first_occurence)  