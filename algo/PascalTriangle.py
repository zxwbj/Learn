# class Solution:
#     def PascalTriangle(self, k):
#         if 0 == k:
#             return [1]
#
#         pl = [0 for i in range(k+1)]
#         pl[0] = 1
#
#         for i in range(1, int(k/2)+1):
#             pl[i] = self.PascalTriangle(k-1)[i] + self.PascalTriangle(k-1)[i-1]
#
#         for i in range(int(k/2)+1, k+1):
#             pl[i] = pl[k-i]
#
#         return pl


# class Solution:
#     def PascalTriangle(self, k):
#         res = [1] + [0] * k
#         for i in range(k):
#             for j in range(i+1, 0, -1):
#                 res[j] = res[j] + res[j-1]
#
#         return res

# class Solution:
#     def PascalTriangle(self, k):
#         p = [1]
#         if not k:
#             return p
#         for j in range(k):
#             p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]
#         return p

# [1, k/1, k/1 * (k-1)/2, k/1 * (k-1)/2 * (k-2)/3, ..., k/1 * (k-1)/2 * (k-2)/3 * ...* 2/(k-1) * 1/k]
class Solution:
    def PascalTriangle(self, k):
        p = [1] * (k+1)
        for i in range(1, int(k/2)+1):
            for j in range(1, i+1):
                p[i] *= float(k+1-j) / float(j)
        for i in range(int(k/2)+1, k+1):
            p[i] = p[k-i]

        p = [int(v+0.5) for v in p]
        return p


if '__main__' == __name__:
    sln = Solution()
    print(sln.PascalTriangle(0))
    print(sln.PascalTriangle(1))
    print(sln.PascalTriangle(2))
    print(sln.PascalTriangle(4))
    print(sln.PascalTriangle(11))
    print(sln.PascalTriangle(36))



