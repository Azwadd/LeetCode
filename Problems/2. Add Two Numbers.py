# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#[9,9,9,9,9,9,9]
#[9,9,9,9]
h1 = ListNode(0)
l1 = h1
for i in range(7):
    l1.next = ListNode(9)
    l1 = l1.next
h1 = h1.next

h2 = ListNode(0)
l2 = h2
for i in range(4):
    l2.next = ListNode(9)
    l2 = l2.next
h2 = h2.next

class Solution:
    def addTwoNumbers(l1, l2):
        head = ListNode(0)
        answer = head
        carry = 0
        while l1 or l2:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            sum = (v1 + v2 + carry)
            digit = sum % 10
            carry = sum // 10
            answer.next = ListNode(digit)
            answer = answer.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry != 0:
            answer.next = ListNode(carry)
            answer = answer.next
        return head.next

    lists = addTwoNumbers(h1,h2)
    while lists:
        print(lists.val)
        lists = lists.next

