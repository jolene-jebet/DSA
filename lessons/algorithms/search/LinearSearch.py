
def linearSearch(array,x):
    for i in range(0,len(array)):
        if array[i] == x:
            return i
    return -1
    
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Position of element" + str(linearSearch(array,3)))

# Time complexity O(n)
