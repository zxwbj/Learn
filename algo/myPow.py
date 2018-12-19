class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        elif n > 0:
            ans = 1.0
            while n > 0:
                if n & 1 == 1:
                    ans *= x
                x *= x
                n = n >> 1
            return ans
        else:
            if n == -2147483648:
                return 1.0 / (self.myPow(x, 2147483647) * x)
            else:
                return 1.0 / self.myPow(x, -n)


if '__main__' == __name__:
    sln = Solution()
    print(sln.myPow(2.0, 10))
    print(sln.myPow(2.1, 3))
    print(sln.myPow(2.0, -2))
    print(sln.myPow(0.00011, 2147483647))
    print(sln.myPow(8.84372, -5))
    print(sln.myPow(34.00515, -3))

