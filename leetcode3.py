# Leetcode Problem 3: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Write your solution below. No code completion suggestions will be shown.

def longest_substring(s: str) -> int:
    n = len(s)
    seen = {}

    max_len = 0
    left = 0

    for right in range(n):
        curr = s[right]

        if curr in seen and left <= seen[curr]:
            left = seen[curr] + 1

        seen[curr] = right

        max_len = max(max_len, right - left + 1)


    return max_len

# Logic
# We are maintaining a dictionary which captures the last seen index of every character
# At any point in time, the current window is between left - right including both ends
# When we come to a character, which we have seen previously
    # Case 1: If the last seen index of this character is out of current active window, then it does not matter
            #Just update the last seen index of this character to right pointer

    # Case 2: If the last seen index of this character is in the current window
        # Meaning seen[curr] >= left
        # Then we need to contract the window from left side
        # We should contract the window by moving the left pointer to one more than its last seen
        # So any and all characters which were before that point will get eliminated from the current active window