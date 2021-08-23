nums = [1, 1, 0, 1, 1, 1]

class Solution:
    def findMaxConsecutiveOnes(nums):
        answer = count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count+=1
                if count > answer:
                    answer = count
        return answer

    print(findMaxConsecutiveOnes(nums))