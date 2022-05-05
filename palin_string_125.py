class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(s.lower().split(" "))
        s1 = "".join([i for i in s1 if i.isalnum()])
        print(s1)
        print(s1[::-1])
        return s1 == s1[::-1]

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))

#check palin