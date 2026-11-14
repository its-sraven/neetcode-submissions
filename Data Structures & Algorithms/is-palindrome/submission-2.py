class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text  = "".join(n for n in s if n.isalnum()).lower()
        return cleaned_text == cleaned_text[::-1]
