class Solution(object):
    def asteroidCollision(self, nums):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # stack =[]
        # for num in nums:
        #     if num > 0:
        #         stack.append(num)
        #     else:
        #         while stack[-1] > 0 and stack[-1] < abs(num):
        #             stack.pop()
        #         if stack and stack[-1] == abs(num):
        #             stack.pop()
        #             continue
        #         if not stack or stack[-1] < 0:
        #             stack.append(num)
        # return stack
        
    
        stack = []
        for asteroid in nums:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)
        return stack


        
        
    
obj=Solution()
print(obj.asteroidCollision([8,-8]))
            
                
