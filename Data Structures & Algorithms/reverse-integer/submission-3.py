class Solution:
    def reverse(self, x: int) -> int:
        if not -2**31 <= x <= 2**31 - 1:
            return 0
        num=str(x)
        if num[0]=="-":
            num=num[0]+num[:0:-1]
        else:
            num=num[::-1]
        result=int(num)
        if not -2**31 <= result <= 2**31 - 1:
            return 0
        return result