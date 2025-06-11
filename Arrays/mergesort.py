def mergesort(array):
    #[1,2,3,4,5,6]
    if len(array) <=1:
        return array
    mid = len(array) //2
    # left = array[:mid]
    # right = array[mid:]
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    return merger(left,right)
    

    return array
def merger(left,right):
    sorted = []
    i,j=0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
    if i != len(left):
        while i != len(left):
            sorted.append(left[i])
            i+=1
        return sorted
    elif j != len(right):
        while j != len(right):
            sorted.append(right[j])
            j+=1
        return sorted


    return sorted
array1 = [1,2,3,5,7,4,6]
array2 = [2,4,5]
print(mergesort(array1))
    