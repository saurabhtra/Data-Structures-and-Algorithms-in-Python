nums = [100,1,200,3,4,2,1]
myset = set(nums)
n= len(nums)
print(myset)
longest = 0

for num in myset:
    if num-1 not in myset:
        x = num
        count = 1
        while x +1 in myset:
            count+=1
            x+=1
        longest = max(longest,count)
print(longest)
