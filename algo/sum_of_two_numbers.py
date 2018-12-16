class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # i = 0
        # while i < len(nums):
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #         j += 1
        #     i += 1

        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i


if '__main__' == __name__:
    sln = Solution();
    print(sln.twoSum([3, 2, 4], 6))

