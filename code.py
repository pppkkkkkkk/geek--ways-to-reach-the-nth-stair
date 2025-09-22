
class Solution:
    def countWays(self, n):
        # # code here
        # if n <= 1:
        #     return n
        # dp = [0]*(n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]
            
        dp = {}
        def recur(n, dp):
            if n <= 2:
                dp[n] = n
                return n
            if n in dp:
                return dp[n]
            ans = recur(n-1, dp) + recur(n-2, dp)
            dp[n] = ans 
            return ans
            
        return recur(n, dp)