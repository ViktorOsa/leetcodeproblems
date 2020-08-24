# task 1

def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    
    if num == 0:
        return 0
    
    if num == 1:
        return arr[0]
    

    result = find_gdc(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        result = find_gdc(result, arr[i])
        
    return result

def find_gdc(num1, num2):
    
    while num2:
        # n1, n2 = 4, 2
        # n1, n2 = 2, 0
        num1, num2 = num2, num1%num2
        
    return num1

# task 2
def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    
    for i in range(days):
        states = next_state(states)    
    
    return states
    
def next_state(state):
    
    result = [0]*8 # left/right end = 0 
    
    result[0] = int(not(0 == state[1]))
    result[7] = int(not(0 == state[6]))
    
    # calculate remaining 6 days
    for i in range(1,len(state)-1):
        result[i] = int((not(state[i-1] == state[i+1])))
        
    print (result)
    
    return result