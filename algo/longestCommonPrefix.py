class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        s0 = strs[0]
        result = ""

        for j in range(len(s0)):
            count = 0
            for v in strs[1:]:
                if j < len(v) and v[j] == s0[j]:
                    count += 1
            if count == len(strs)-1:
                result += s0[j]
            else:
                return result

        return result


if '__main__' == __name__:
    sln = Solution()
    print(sln.longestCommonPrefix(["123", ""]))
    print(sln.longestCommonPrefix(["aca", "cba"]))
    print(sln.longestCommonPrefix(["dog", "racecar", "car"]))

