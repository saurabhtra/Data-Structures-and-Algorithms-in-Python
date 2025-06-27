class Solution:
	def minCoins(self, coins, sum):
		# code here
		cnt = 0
		tsum =0
		coins.sort(reverse=True)
		for i in range(len(coins)):
			if tsum ==sum:
				return cnt
			while tsum+coins[i] <= sum:
				cnt+=1
				tsum+=coins[i]
			if tsum > sum:
				cnt-=1
				tsum-=coins[i]
		print(tsum ,cnt)
dommy = Solution()
dommy.minCoins([25,5,15],30)