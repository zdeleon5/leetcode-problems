class Solution:
    def isPalindrome(self, s: str) -> bool:

        s2 = "".join(char for char in s if char.isalnum()).lower()

        l, r = 0, len(s2) - 1

        print(s2)

        while r >= l: 
            if s2[l] == s2[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True

  # Roadblocks: string immutability/methods
