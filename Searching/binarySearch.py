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
    


if __name__ == "__main__" :

    import array
    a = array.array('i',[ ])
    n = int(input("Enter the no of elements of array : "))
    for i in range (0,n):
        b = int(input("Enter the elemens of array : "))
        a.append(b)
    low = 0
    high = n-1
    key = int(input("Enter the element to be found : "))
    arr = sorted(a)
    print(arr)
    print(binary_Search(arr,low,high,key))
