class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        s1 = "racecar"
        s2 = "carrace"
        sol = Solution()
        print(sol.isAnagram(s1, s2)) # Output: True