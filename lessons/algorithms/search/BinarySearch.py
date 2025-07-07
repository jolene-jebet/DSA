# Iterative Binary Search Algorithm
def binarySearchIterative(array,x):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low) + (high - low) // 2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [2, 3, 4, 10, 40]
print("Position of element at " + str(binarySearchIterative(arr,40)))

"""
    Phase 1: 
        Low = 0
        High = 4
        mid = 2
    Phase 2:
        Low = 2 + 1 = 3
        High = 4
        mid = (3 + (4 - 3)) // 2 = 3
    Phase 3:
        Low = 3 + 1 = 4
        High = 4
        mid = (4 + (4 - 4)) = 4
"""

def binarySearchRecursive(array,low,high,x):
    if high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearchRecursive(array,low,mid - 1,x)
        else:
            return binarySearchRecursive(array,mid+1,high,x)
    else:
        return -1
            
print("Binary Search using recursive edition " + str(binarySearchRecursive(arr,0,len(arr) - 1,2)))

"""
    Binary Search:
        Time Complexity:
            1. Best Case O(1)
            2. Average Case: O(log N)
            3. Worst Case: O(log N)
        Space Complexity:
            1. O(1)

    Applications:
        1. Used in machine learning algos e.g. training neural networks or finding optimal hyperparameters for a model
        2. Searching a database
        3. Can be used for searching in computer graphics
"""