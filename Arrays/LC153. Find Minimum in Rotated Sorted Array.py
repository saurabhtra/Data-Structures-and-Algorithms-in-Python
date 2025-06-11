def findMin(nums):
    low = 0
    n= len(nums)
    high = n-1
    mini =float("inf")
    # if n ==1:
    #     return nums[0]
    while low <= high:
        mid = (low+high)//2
        # find the sorted part
        if nums[mid] >= nums[low]:
            mini =min(mini,nums[low])
            low = mid+1
        else:
            mini = min(mini,nums[mid])
            high = mid-1
    return mini


nums = [1]
print(findMin(nums))
