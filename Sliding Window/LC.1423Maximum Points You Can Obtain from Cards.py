nums = [1,2,3,4,5,6,1]
k = 3
n= len(nums)
leftsum =0
rightsum =0
maxi=0
l,r =0,n-1
for _ in range(k):
    leftsum +=nums[l]
    l+=1
maxi =max(maxi,leftsum)
print(maxi)
for _ in range(k):
    leftsum -= nums[l-1]
    print("nums[l],nums[r]",nums[l-1],nums[r])
    rightsum += nums[r]
    print("leftsum, rightsum", leftsum,rightsum)
    l-=1
    r-=1
    maxi=max(maxi,leftsum+rightsum)
print(maxi)

