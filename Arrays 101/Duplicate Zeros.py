arr = [1,0,2,3,0,4,5,0]

class Solution:
    def duplicateZeros(arr):
        i = 0
        while i < len(arr):
            if arr[i] != 0:
                i += 1
            else:
                arr.insert(i, 0)
                arr.pop(len(arr)-1)
                i += 2
        return arr

    print(duplicateZeros(arr))