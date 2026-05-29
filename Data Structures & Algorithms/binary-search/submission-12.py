class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r: 
            m=(l+r) // 2
            if nums [m] > target:
                r = l - 1 
            elif nums [m] < target: 
                l = r + 1
            else: 
                return m 
        return m -1

