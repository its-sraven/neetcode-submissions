class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = [itm for itm in nums if itm == target]
        if res:
            return nums.index(res[0])
        else:
            return -1