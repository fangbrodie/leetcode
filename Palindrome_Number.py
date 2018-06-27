class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            cache = []
            while x > 0:
                cache.append(x % 10)
                x = x // 10
            size = len(cache)
            i = 0
            j = size - 1
            while i < j:
                if cache[i] != cache[j]:
                    return False
                i += 1
                j -= 1
            return True

a = Solution()
b = 59495
print(a.isPalindrome(b))