class Solution(object):
    def convert(self, s, numRows):

        if 1 == numRows:
            return s

        ss = [''] * min(numRows, len(s))
        curr = 0

        for v in s:
            ss[curr] += v

            if 0 == curr:
                godown = True
            elif numRows-1 == curr:
                godown = False

            if godown:
                curr += 1
            else:
                curr -= 1

        return ''.join(ss)


if '__main__' == __name__:
    sln = Solution()
    print(sln.convert('LEETCODEISHIRING', 100))
    print(sln.convert('LEETCODEISHIRING', 2))
