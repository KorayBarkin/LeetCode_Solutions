class Solution(object):
    def isPalindrome(self, x):
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10
        if reversed_num == x:
            return True
        else:
            return False