class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):        
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[i] + A[j] == B:
                    return 1
        return 0