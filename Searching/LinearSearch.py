def linear_Search(arr,key):
    
    '''
    linear search algorithm
    Time Complexity = O(n)
    Space Complexity = O(1)
    '''

    for i in range (0,len(arr)):
        if arr[i] == key:
            return f"Element is found at index position {i}"
    return "The element doesn't exist"

if __name__ == "__main__":

    import array
    a = array.array('i',[])
    n = int(input("Enter the no.of elements : "))
    for i in range (0,n):
        b = int(input("Enter the elements of array : "))
        a.append(b)
    key = int(input("Enter the element to be found :"))
    print(linear_Search(a,key))
