class Solution:
    def PascalTriangle(self, k):
        if 0 == k:
            return [1]
        elif 1 == k:
            return [1, 1]
        elif 2 == k:
            return [1, 2, 1]

        pl = [0 for i in range(k+1)]
        pl[0] = 1
        for i in range(1, int(k/2)+1):
            pl[i] = self.PascalTriangle(k-1)[i] + self.PascalTriangle(k-1)[i-1]
        for i in range(int(k/2)+1, k+1):
            pl[i] = pl[k-i]

        return pl


if '__main__' == __name__:
    sln = Solution()
    print(sln.PascalTriangle(0))
    print(sln.PascalTriangle(1))
    print(sln.PascalTriangle(2))
    print(sln.PascalTriangle(3))
    print(sln.PascalTriangle(4))
    print(sln.PascalTriangle(5))
    print(sln.PascalTriangle(6))
    print(sln.PascalTriangle(7))
    print(sln.PascalTriangle(8))

