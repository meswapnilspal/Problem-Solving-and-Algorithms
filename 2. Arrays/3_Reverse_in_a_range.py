class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        t = 0
        while (B<C):
            t = A[B]
            A[B] = A[C]
            A[C] = t
            #swap(A[B],A[C])
            B += 1
            C -= 1
        return A