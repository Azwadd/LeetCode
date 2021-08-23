one = [555,901,482,1771]
two = [100000]

class Solution:
    def findNumbers(nums):
        answer = 0
        for i in range(len(nums)):
            number = nums[i]
            count = 0
            while number > 0:
                number = int(number / 10)
                count += 1
            if count % 2 == 0:
                answer += 1
        return answer

    print("result should be 1, result: " + str(findNumbers(one)))
    print("result should be 1, result: " + str(findNumbers(two)))