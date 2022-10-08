class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mx = max(A)
        cntr = 0
        for i in A:
            if i == mx:
                cntr += 1
        return(len(A)-cntr)
