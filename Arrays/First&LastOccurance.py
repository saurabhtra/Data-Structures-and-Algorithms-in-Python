nums=[1,2,3,3,4,5]
target = 3
lb = -1
n= len(nums)
left =0
right = n-1
while left <= right:
    mid = (left+right) //2
    if nums[mid] >= target:
        lb=mid
        right = mid -1
    else:
        left = mid+1
left = 0
right = n-1
ub = n-1
while left <= right:
    mid =(left+right)//2
    if nums[mid] <= target:
        left = mid +1
    else:
        ub = mid
        right = mid -1

print(lb)

print(ub)


