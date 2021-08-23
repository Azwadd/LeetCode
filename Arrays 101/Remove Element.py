nums = [3,2,2,3]
val = 3

class Solution:
    def removeElement(nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        print(len(nums))
        print(nums)
        return len(nums)

    removeElement(nums, val)
