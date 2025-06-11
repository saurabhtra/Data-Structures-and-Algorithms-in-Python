nums1 = [5,6,7,0,0,0]
m = 3
nums2 = [1,2,10]
n = 3

def merger(nums1,m,nums2,n):
    # method 1
#     i = m -1
#     j = n-1
#     last = m+n-1
#     if m==0:
#         if n==0:
#             return
#         for idx in range(n):
#             nums1[idx] = nums2[idx]
#     while j >= 0 and i >= 0:
#         if(nums1[i] > nums2[j]):
#             nums1[last] = nums1[i]
#             last -= 1
#             i -=1
#         else:
#             nums1[last] = nums2[j]
#             last -=1
#             j-=1
#     while j>=0 :
#         nums1[last] = nums2[j]
#         last -=1
#         j-=1
# merger(nums1,m,nums2,n)
# print(nums1)
    #method 2
    for n in nums2:
        nums1[m] = n
        m+=1
    nums1.sort()
merger(nums1,m,nums2,n)
print(nums1)
 