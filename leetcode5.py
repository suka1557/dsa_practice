# Leetcode Problem 5: Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Example 3:
# Input: s = "a"
# Output: "a"

# Example 4:
# Input: s = "ac"
# Output: "a"
# Explanation: "c" is also a valid answer.

# Write your solution below. No code completion suggestions will be shown.

#   a    b    b   a  c

def check_pal_even(index: int, s: str) -> int:
    left, right = index - 1, index
    n = len(s)
    current_len = 0
    while left > -1 and right < n:
        if s[left] == s[right]:
            current_len += 2
        else:
            break
        left, right = left - 1, right + 1

    return current_len

def even_len_pal(s: str):  
    n = len(s)

    if n < 2:
        return 0
    
    max_even_len = 0
    max_index = -1

    for i in range(1, n):
        even_len =  check_pal_even(i, s)
        if even_len > max_even_len:
            max_even_len = even_len
            max_index = i

    return max_even_len, max_index

def check_pal_odd(index: int, s: str) -> int:
    n = len(s)
    left, right = index - 1, index + 1
    current_len = 1

    while left > -1 and right < n:
        if s[left] == s[right]:
            current_len += 2
        else:
            break
        left, right = left - 1, right + 1

    return current_len


def odd_len_pal(s: str):
    #Edge cases
    if s == "":
        return 0, -1
    
    n = len(s)
    
    max_odd_len = 0
    max_index = -1

    for i in range(n):
        odd_len =  check_pal_odd(i, s)
        if odd_len > max_odd_len:
            max_odd_len = odd_len
            max_index = i

    return max_odd_len, max_index
    


def longestPalindrome( s: str) -> str:
    # Placeholder for the solution
    if s is None or s == "":
        return s
    
    max_odd_len, max_odd_index = odd_len_pal(s)
    print(f"------ Odd Characs -----------, Index: {max_odd_index}, Length: {max_odd_len}")

    max_even_len, max_even_index = even_len_pal(s)
    print(f"------ Even Characs -----------, Index: {max_even_index}, Length: {max_even_len}")

    if max_odd_len >= max_even_len:
        half_part = (max_odd_len - 1) // 2
        left_index = max_odd_index - half_part
        right_index = max_odd_index + half_part
        return s[left_index: right_index + 1]
    
    else:
        half_part = max_even_len // 2
        half_left = max_even_index - half_part
        half_right = max_even_index + half_part - 1
        print(half_left, half_right)
        return s[half_left : half_right + 1]
    
print(longestPalindrome("abcddcba"))