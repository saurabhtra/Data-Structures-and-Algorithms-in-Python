nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
maxi = 0
k=2
i,j=0,0
n= len(nums)
zeros = 0
while j < n:
    if nums[j] == 0:
        zeros+=1
    if zeros > k:
        if nums[i] ==0:
            zeros-=1
        i+=1
    if zeros <=k:
        maxi=max(maxi,j-i+1)
    j+=1
print(maxi)



