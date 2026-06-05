def interpolation_Search(arr,key):
    
    '''
    interpolation search algorithm
    time complexity =O(log(logn))
    space complexity = O(1)
    '''
    
    low = 0
    high = len(arr)-1
    pos = low + int(((key -arr[low])*(high-low))/(arr[high]-arr[low]))
    return f"The element is found at index position {pos}."

if __name__ == "__main__":
    import array
    a = array.array('i',[ ])
    n = int(input("Enter the no.of elements : "))
    for i in range (n):
        b = int(input("Enter the elements of array (for interpolation Search) : "))
        a.append(b)
    key = int(input("Enter the element to be found : "))
    print("Array : ", a.tolist())

    print(interpolation_Search(a,key))
