class Solution(object):
    def asteroidCollision(self, nums):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        "[4 ,7,1,1,2,-3,-7,17,15,-18,-19]"
        stack =[]
        for num in nums:
            if num > 0:
                stack.append(num)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(num):
                    stack.pop()
                if stack and stack[-1] == abs(num):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(num)
                   
            
            
        return stack
    
obj=Solution()
print(obj.asteroidCollision([-7,17]))
            
                
