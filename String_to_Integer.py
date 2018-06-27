class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        flag = False
        res = ""
        for i in str:
            if i in "-+ ":
                if flag:
                    if res in "-+ " or res is "":
                        return 0
                    elif int(res) < -2147483648:
                        return -2 ** 31
                    elif int(res) > 2147483647:
                        return 2147483647
                    return int(res)
                elif i in "-+":
                    flag = True
                if res is not "":
                    if res is "-":
                        return 0
                    elif int(res) < -2147483648:
                        return -2 ** 31
                    elif int(res) > 2147483647:
                        return 2147483647
                    return int(res)
                if res is "":
                    if i is "-":
                        res += i
            elif i in "1234567890":
                res += i
            else:
                if res is "-" or res is "":
                    return 0
                elif int(res) < -2147483648:
                    return -2147483648
                elif int(res) > 2147483647:
                    return 2147483647
                return int(res)

        if res is "-" or res is "":
            return 0
        elif int(res) < -2147483648:
            return -2147483648
        elif int(res) > 2147483647:
            return 2147483647
        return int(res)

a = Solution()
b = "    -88827   5655  U"
print(a.myAtoi(b))