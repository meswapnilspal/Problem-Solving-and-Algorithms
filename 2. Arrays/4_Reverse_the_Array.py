class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        A = list(A)
        t = 0
        B = 0
        C = int(len(A)-1)
        while (B<C):
            t = A[B]
            A[B] = A[C]
            A[C] = t
            #swap(A[B],A[C])
            B += 1
            C -= 1
        return A
