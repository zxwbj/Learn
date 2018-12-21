class Solution(object):
    def myAtoi(self, str):
        str = str.strip()
        if '' == str or '+' == str or '-' == str:
            return 0

        signs = ('++', '--', '+-', '-+')
        if str[:2] in signs:
            return 0

        ss = str[0]
        chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

        if ss not in chars and ss not in ('+', '-'):
            return 0

        for v in str[1:]:
            if v in chars:
                ss += v
            else:
                break

        if ss == '-' or ss == '+':
            return 0

        num = int(ss)
        if num > 2147483647:
            num = 2147483647
        elif num < -2147483648:
            num = -2147483648

        return num


if '__main__' == __name__:
    sln = Solution()
    print(sln.myAtoi('42'))
    print(sln.myAtoi('    -42'))
    print(sln.myAtoi('4193 with words'))
    print(sln.myAtoi('words and 987'))
    print(sln.myAtoi(''))
    print(sln.myAtoi('+-2'))
    print(sln.myAtoi('-abc'))
    print(sln.myAtoi('0-1'))

