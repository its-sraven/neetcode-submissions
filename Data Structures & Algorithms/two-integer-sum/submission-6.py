class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target - num[1] = num[j]
        #9 - 5 = 4
        out = list()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j]  == target:
                    out.append(i)
                    out.append(j)
                    return out