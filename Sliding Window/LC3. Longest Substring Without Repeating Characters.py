class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi=0
        # for i in range(len(s)):
        #     myset=set()
        #     for j in range(i,len(s)):
        #         if s[j] not in myset:
        #             myset.add(s[j])
        #             maxi=max(maxi,j-i+1)
        #         else:
        #             break
        left,right=0,0
        mydic={}
        while right < len(s):
            if s[right] in mydic:
                left  = max(left,mydic[s[right]]+1)
            mydic[s[right]] = right
            maxi=max(maxi, right-left+1)
            right+=1
        return maxi
    
s="cadbzabcd"
obj=Solution()
print(obj.lengthOfLongestSubstring(s))
