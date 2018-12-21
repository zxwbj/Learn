# class Solution:
#     def constructRectangle(self, area):
#
#         def getFactor(self, num):
#             LF = []
#             for i in range(2, int(num/2)+1):
#                 if num % i == 0:
#                     LF.append(i)
#             return LF
#
#         Fa = getFactor(self, area)
#         print(Fa)
#         result = [area, 1]
#         min = area - 1
#
#         for w in Fa:
#             l = area // w
#             if l < w:
#                 break
#             elif l - w < min:
#                 result = [l, w]
#                 min = l - w
#
#         return result

import math
class Solution:
    def constructRectangle(self, area):

        L = int(math.sqrt(area))
        W = int(math.sqrt(area))
        if L * W == area:
            return [L, W]

        result = [area, 1]
        for i in range(L, 1, -1):
            j = area // i
            if i * j == area:
                return [j, i]
        return result


if '__main__' == __name__:
    sln = Solution()
    print(sln.constructRectangle(6))
