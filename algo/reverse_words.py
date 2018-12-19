class Solution(object):
    def reverseWords(self, s):

        ss = s.split(' ')

        sss = [v for v in ss if '' != v]
        # for v in ss:
        #     if v != '':
        #         sss.append(v)

        return ' '.join(sss[::-1])


if '__main__' == __name__:
    sln = Solution()
    print(sln.reverseWords('   the     sky    is    blue   '))
