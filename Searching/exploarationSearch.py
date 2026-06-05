def exploration_Search(arr,key):

    '''
    exploration search algorithm
    time complexity =O(logn)
    space complexity =O(logn)
    '''
    n = len(arr)
    if arr[0] == key:
        return f"The element is found at inder position 0."
    i = 1
    while i<n and arr[i]<key:
        i = i*2
    left = i//2
    right =min(i,n-1)
    
    return binary_Search(arr,left,right,key)

def binary_Search(arr,low,high,key):
    
    '''
    binary search algorithm
    time complexity =O(log(n))
    space complexity = O(1)
    '''

    if low >high :
        return "The element doesn't exist." 
    mid = ((low-high)//2)+high
    if arr[mid] == key:
        return f"The element is found at index position {mid} after sorting."
    elif arr[mid] <key:
         return binary_Search(arr,mid+1,high,key)
    else:
        return binary_Search(arr,low,mid-1,key)


if __name__ == "__main__":
    import array
    a = array.array('i',[ ])
    n = int(input("Enter the no.of elements : "))
    for i in range (n):
        b = int(input("Enter the elements of array (for exploration search) : "))
        a.append(b)
    key = int(input("Enter the element to be found : "))
    print("Array : ", a.tolist())

    print(exploration_Search(a,key))

        
