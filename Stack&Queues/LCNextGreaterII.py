class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]
        mini=float("inf")
        ans=[-1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if not stack:
                stack.append(nums[i])
            else:
                while stack and stack[-1] >= nums[i]:
                    stack.pop()
                stack.append(nums[i])
        

        print(stack)
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] >= nums[i]:
                stack.pop()
            if stack:
                ans[i] =stack[-1]
            stack.append(nums[i])
        print(ans)

nums = [1,2,3,4,3]
obj=Solution()
obj.nextGreaterElements(nums)