class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        c=0
        i=2
        while(i*i<=A):
            if A%i == 0:
                if i == A/i:
                    c += 1
                else:
                    c += 2
            i += 1
        c +=2
        return c