class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        s = s.split(' ')
        for el in s:
            res += el[::-1] + ' '
        res = res.rstrip()
        return res
