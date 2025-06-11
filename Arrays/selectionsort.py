def selSort(array):
    flag = False
    for i in range(len(array)):
        min_index = i
        
        for j in range(i+1,len(array)):
            
            print(array[j], "  ", array[min_index],array[i])
            if array[j] < array[min_index]:
                min_index = j
                flag = True
                # print("min element = ",array[min_index])
                
        if flag == True:
            # print("swap",array[i],array[min_index])
            array[i],array[min_index] = array[min_index], array[i]
            flag = False
    return array

array = [1,2,4,3,5,6]
print(selSort(array))

