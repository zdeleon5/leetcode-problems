class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        if len(nums) == 0:
            return

        if len(nums) == 1: 
            return nums[0]

        for num in nums:
            if num not in hm:
                hm[num] = 1
            else: 
                hm[num] += 1

        return max(hm, key=hm.get)

# roadblock: getting max value from a dict based on value
