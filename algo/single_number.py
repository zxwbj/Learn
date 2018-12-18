

class Solution():
    def SingleNumber(self, nums):
        ans = 0
        for v in nums:
            ans ^= v
        return ans


if '__main__' == __name__:
    sln = Solution()
    print(sln.SingleNumber([1, 2, 3, 3, 1]))
