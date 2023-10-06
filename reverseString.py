class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1

        while i < j:
            s[j], s[i] = s[i], s[j]
            i += 1
            j -= 1
        return s