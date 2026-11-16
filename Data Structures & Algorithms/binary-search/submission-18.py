class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = [i for i,n in enumerate(nums) if n == target]
        return res[0] if res else -1