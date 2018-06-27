class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size1 = len(nums1)
        size2 = len(nums2)
        size = size1 + size2
        sort_nums = []
        i = 0
        j = 0
        k = 0
        median = size // 2
        while i < size1 and j < size2 and k < median + 1:
            if nums1[i] < nums2[j]:
                sort_nums.append(nums1[i])
                i += 1
            else:
                sort_nums.append(nums2[j])
                j += 1
            k += 1
        while i < size1 and k < median + 1:
            sort_nums.append(nums1[i])
            i += 1
            k += 1
        while j < size2 and k < median + 1:
            sort_nums.append(nums2[j])
            j += 1
            k += 1

        if bin(size)[-1] == "1":
            return sort_nums[median]
        else:
            return (sort_nums[median - 1] + sort_nums[median])/2.0

a = Solution()
b = [3, 6, 8]
c = [4, 5]
print(a.findMedianSortedArrays(b, c))