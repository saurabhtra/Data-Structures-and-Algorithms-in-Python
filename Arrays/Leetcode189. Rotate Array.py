def reverse(array,start,end):
    if start >= end :
        return 
    array[start],array[end]  = array[end],array[start] 
    reverse(array,start+1,end-1)

array = [1,2,3,4,5,6,7]
reverse(array,0,3)
print(array)

#now write funtion to rotate the array 'k' time k >0 and k is intyet
def reverser(nums,start,end):
    while start < end :
        nums[start],nums[end] = nums[end],nums[start]
        start +=1
        end -=1

    return
nums = [1,2,3,4,5,6,7]
reverser(nums,0,n-1-k-1 )