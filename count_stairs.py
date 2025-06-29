class Solution:
    def climbStairs(self, n: int) -> int:
        dict = {0:0,
                1:1,
                2:2
                }
        
        def back(n):
            if n in dict:
                return dict[n]
            if n-1 not in dict:
                dict[n-1] = back(n-1)
            if n-2 not in dict:
                dict [n-2] = back(n-2)
            return dict[n-2]+dict[n-1]
        return back(n)