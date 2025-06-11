def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    low = 0
    n= len(nums)
    high = n-1
    while low <= high:
        mid = (low+high) //2
        if nums[mid] ==target:
            return True
        if nums[mid]==nums[low]==nums[high]:
            low+=1
            high-=1
            continue
        if nums[mid] <= nums[high]:
            if nums[mid] < target and target<=nums[high]:
                low = mid+1
            else:
                high = mid-1
        else:
            if nums[low] <= target and target < nums[mid]:
                high = mid-1
            else :
                low = mid+1
    return False
nums=[1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]
target = 13
print(search(nums,target))