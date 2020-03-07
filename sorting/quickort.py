"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array, low, high):
    if low < high:
        pi = partition (array, low , high)
        
        
        quicksort(array, low , pi - 1)
        quicksort(array, pi + 1, high)
        
    return array

def partition(array, low , high):
    pi = array[high]
    
    i = low - 1
    
    for j in range(low, high):
        
        if (array[j] < pi ):
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i+1] , array[high] = array[high], array[i+1]

    #print (array[low:high+1])
    
    return i+1

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test, 0, len(test)-1))