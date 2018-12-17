class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0
        L = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                L.append(nums1[i])
                i += 1
            else:
                L.append(nums2[j])
                j += 1

        while i < len(nums1):
            L.append(nums1[i])
            i += 1

        while j < len(nums2):
            L.append(nums2[j])
            j += 1

        length = len(L)
        if 1 == length % 2:
            median = L[int((length-1)/2)]
        else:
            median = (L[int(length/2)] + L[int(length/2-1)])/2

        return median


if '__main__' == __name__:
    sln = Solution()
    print(sln.findMedianSortedArrays([1, 2, 4, 7, 9, 10], [2, 5, 6]))
