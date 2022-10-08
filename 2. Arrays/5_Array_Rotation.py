class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        B = B%(len(A))
        def reverse(X, Y, Z):
            t = 0
            while (bool(Y<Z)):
                t = X[Y]
                X[Y] = X[Z]
                X[Z] = t
                #swap(A[B],A[C])
                Y += 1
                Z -= 1
            return X
       
        s1 = reverse(A, 0, len(A)-1)       
        s2 = reverse(s1, 0, B-1)        
        s3 = reverse(s2, B, len(A)-1)
        return s3