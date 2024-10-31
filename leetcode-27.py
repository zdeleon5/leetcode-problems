class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1, p2 = 0, len(nums) - 1
        counter = 0
        while p2 >= p1:
            if nums[p2] == val:
                nums[p2] = "_"
                p2 -= 1
            elif nums[p1] == val and nums[p2] != val:
                nums[p1] = nums[p2]
                nums[p2] = "_"
                p2 -= 1
                p1 += 1
                counter += 1
            else:
                p1 += 1
                counter += 1

        return counter

# FIRST SOLUTION REFLECTION
# roadblocks: handling the two pointer approach. i forgot to increment the p1 pointer as the else case. 
