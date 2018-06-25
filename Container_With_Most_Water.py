class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        size = len(height) - 1
        hl = 0
        hr = 0
        max = 0
        while(l < r):
            if height[l] > height[r]:
                s = size * height[r]
                r -= 1
            else:
                s = size * height[l]
                l += 1
            size -= 1
            if s > max:
                max = s
        return max

a = Solution()
b = [3,4,5]
print(a.maxArea(b))