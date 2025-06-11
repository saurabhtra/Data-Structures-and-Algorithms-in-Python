class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        self.stack=[]
        self.dic ={}
        n2=len(nums2)-1
        ans=[]
        for i in range(n2,-1,-1):
            while len(self.stack) != 0 and nums2[i] >= self.stack[-1]:
                self.stack.pop()
            print(i)
            if len(self.stack) != 0:
                self.dic[nums2[i]]=self.stack[-1]
                print("self.dic[i]=self.stack[-1]",self.dic[nums2[i]],self.stack[-1])
            self.stack.append(nums2[i])
        print(self.dic)
        for n in nums1:
            ans.append(self.dic.get(n,-1))
        return ans
obj =Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(obj.nextGreaterElement(nums1,nums2))