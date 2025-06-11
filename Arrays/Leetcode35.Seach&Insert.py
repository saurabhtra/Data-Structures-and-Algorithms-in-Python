nums = [1,3,5,6]
target = 6
pos = -1
l = 0
r = len(nums)-1
mid = -1
ans = 0
while l <= r:
    mid =(l+ r) // 2
    print("num[mid[] = ",nums[mid],end=" ")
    print("nums[mid] < target",nums[mid] <target )

    if nums[mid] < target:
        print(" r = ", r)
        l =mid+1
    elif nums[mid] > target:
        print("l= ",l)
        r = mid -1
    else:
        break
    
print(mid)