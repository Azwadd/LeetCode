s = "pwwkew"


class Solution(object):
    def lengthOfLongestSubstring(s):
        max = count = i = 0
        letters = []
        # Iterate through the string to find the longest substring without repeating characters
        while i in range(len(s)):
            # Normal case - no repeating letters yet so we increment count and add the letter to the list of letters
            if s[i] not in letters:
                letters.append(s[i])
                count += 1
                i += 1
            else:
                if count > max:
                    max = count
                letters.clear()
                count = 0
                j = i -1
                while s[j] != s[i]:
                    j -= 1
                i = j + 1
        if count > max:
            max = count
        return max
    print(lengthOfLongestSubstring(s))
