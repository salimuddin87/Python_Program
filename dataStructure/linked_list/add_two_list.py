from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_digit(a, b, c):
    num = a + b + c
    if num > 9:
        val = num % 10
        carry = int(num / 10)
    else:
        val = num
        carry = 0
    return val, carry


def append_ll(r, t):
    temp = ListNode(val=t)
    last = r

    if r is None:
        return temp

    while last.next is not None:
        last = last.next

    last.next = temp
    return r


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = None
        while True:
            if l1 and l2:
                val, carry = add_two_digit(l1.val, l2.val, carry)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val, carry = add_two_digit(l1.val, 0, carry)
                l1 = l1.next
            elif l2:
                val, carry = add_two_digit(0, l2.val, carry)
                l2 = l2.next
            else:
                break

            result = append_ll(result, val)

        if carry > 0:
            result = append_ll(result, carry)

        return result


if __name__ == "__main__":
    print(add_two_digit(5,2,1))
