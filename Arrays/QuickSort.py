# it will put pivot in its correct position
#num =[4,1,2,3,5,6,7] pivot = 4 low = 0 , high = len(nums)-1
def partition(nums,low,high):
    i= low
    j = high
    pivot = nums[low]
    while i < j:
        while nums[i] <= pivot and i <= high -1:
            i+=1
        while nums[j] > pivot and j >= low+1:
            j-=1
        if i <j :
            nums[i],nums[j] = nums[j],nums[i]
    nums[low],nums[j] = nums[j],nums[low]
    
    return j
def quic_sort(nums,low,high):
    if low < high:
        pidx = partition(nums,low,high)
        quic_sort(nums,low,pidx-1)
        quic_sort(nums,pidx+1,high)
nums = [9,1,2,3,5,6,7]
quic_sort(nums,0,len(nums)-1)
print(nums)

