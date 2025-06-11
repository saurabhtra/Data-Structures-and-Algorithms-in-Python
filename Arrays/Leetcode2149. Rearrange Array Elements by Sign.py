nums = [3,1,-2,-5,2,-4]
# brute force method
# pos = []
# neg = []
# for num in nums:
#     if num > 0:
#         pos.append(num)
#     else:
#         neg.append(num)
# ans = []
# for i in range(len(pos)):
#     ans.append(pos[i])
#     ans.append(neg[i])
# print(ans)

# optimal
p = 0
n = 1
length = len(nums)
result = [0]*length
print(result)
for i in range(length):
    num = nums[i]
    if num > 0:
        result[p] = num
        p+=2
    else:
        result[n] = num
        n+=2
print(result)
    
