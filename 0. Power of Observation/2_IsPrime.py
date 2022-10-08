class Solution:
    # @param A : long
    # @return an integer
    def solve(self, A):        
        i = 2
        ans = 1
        while(i*i<=A):
            if A%i == 0:
                ans = 0
                break           
            i+=1
        if A == 1:
            ans = 0
        return ans
