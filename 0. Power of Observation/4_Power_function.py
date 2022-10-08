class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def power(self, A, B):
        prod = 1
        for i in range(B):
            prod = prod * A
        return prod