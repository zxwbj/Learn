class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        head = 0
        tail = 1
        max = 1

        while tail < len(s):

            while s[tail] in s[head:tail]:
                head += 1

            while s[tail] not in s[head:tail]:
                if max < tail - head + 1:
                    max = tail - head + 1

                tail += 1
                if tail >= len(s):
                    break

        return max


if '__main__' == __name__:
    sln = Solution()
    print(sln.lengthOfLongestSubstring('abcabcbb'))
    print(sln.lengthOfLongestSubstring('pwwkew'))
    print(sln.lengthOfLongestSubstring('ccccccc'))
