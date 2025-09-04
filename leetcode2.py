# Leetcode Problem 2: Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Write your solution below. No code completion suggestions will be shown.

# ...existing code...

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode(-1)
    start = l3

    carry = 0
    while l1 and l2:
        total = l1.val + l2.val + carry
        if total >= 10:
            carry = 1
            total = total % 10
        else:
            carry = 0

        l3.next = ListNode(total)

        l1, l2, l3 =  l1.next, l2.next, l3.next

    if l1:
        while l1:
            total = l1.val + carry
            if total >= 10:
                carry = 1
                total = total % 10
            else:
                carry = 0

            l3.next = ListNode(total)
            l1, l3 = l1.next, l3.next

    if l2:
        while l2:
            total = l2.val + carry
            if total >= 10:
                carry = 1
                total = total % 10
            else:
                carry = 0

            l3.next = ListNode(total)
            l2, l3 = l2.next, l3.next

    #Edge Case
    # l1:[5], l2:[5] --> [0] -> [1]
    if carry:
        l3.next = ListNode(carry)

    return start.next
