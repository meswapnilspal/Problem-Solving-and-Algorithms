class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        i = 1
        while(i*i<=A):
            if i*i==A:
                ans = i
            else:
                ans = -1
            i += 1
        return ans