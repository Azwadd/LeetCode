nums = [-4,-1,0,3,10]

class Solution:
    def sortedSquares(nums):
        answer = []
        for i in range(len(nums)):
            answer.append(nums[i]**2)
        return sorted(answer)

    print(sortedSquares(nums))