class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        for i,itm in enumerate(nums):
            if target in nums :
                if target ==  itm:
                    res = i
            else:
                return -1
        return res
        