from jovian.pythondsa import evaluate_test_cases

# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.


#########################  Problem #########################################
# We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.

########################   Input   ############################################
# cards: A list of numbers sorted in decreasing order. E.g. [13, 11, 10, 7, 4, 3, 1, 0]
# query: A number, whose position in the array is to be determined. E.g. 7

#######################    Output   ###########################################
# position: The position of query in the list cards. E.g. 3 in the above case (counting from 0)


def binarySearch(cards, query):

    low, high,  position = 0, len(cards)-1, -1  
    
    while low <= high:
        
        mid = (low+high)//2
    
        if(mid > 0):
            if(cards[mid]== query and cards[mid-1]> query ):
                position=mid
                break
            elif (cards[mid] > query ):
                low = mid+1
            else: 
                high= mid-1
        else:
            if(cards[mid]== query ):
                position=mid
                break
        
    return position


##Tests
tests = []

tests.append({
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
})


# query occurs in the middle

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

# cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})



# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})


# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

 
# k = 0
# while k <= len(tests):
#     print(binarySearch(tests[0]["input"]["cards"],tests[0]["input"]["query"] ) == tests[0]['output'])
#     k+=1

evaluate_test_cases(binarySearch, tests)