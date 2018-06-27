class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000

        while num > 0:
            num / M