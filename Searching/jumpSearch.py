import math
import array
def jump_Search(arr,key):
    
    '''
    jump search algorithm
    time complexity = O(root(n))
    space complixity = O(1)
    '''

    n = len(arr)

    step = math.floor(math.sqrt(n))
    previous = 0
    
    while arr[min(step,n-1)] <key:
        previous = step
        step += math.floor(math.sqrt(n))
        if previous > n:
            return "The element doesn't exist ."

    while arr[previous] < key:
        previous += 1

        if previous == min(step,n):
            return "The element doesn't exist ."

    if arr[previous] == key:
        return f" The element is found at index position {previous} after sorting ."

    return "The element doesn't exist ."


if __name__ == "__main__":

    a = array.array('i',[ ])
    n = int(input("Enter the no.on elements in the array : "))
    for i in range(n):
        b = int(input("Enter the elements of array : "))
        a.append(b)
    
    key = int(input("Enter the element to be found : "))
    arr = sorted(a)
    print("Sorted_array : ",arr)

    print(jump_Search(arr,key))
          
