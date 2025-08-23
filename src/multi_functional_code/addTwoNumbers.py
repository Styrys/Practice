from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

#main function to add two numbers represented by linked lists
def printList(node: Optional[ListNode]):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

def createList(nums):
    dummy = ListNode(0)
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    l1_input = input("Enter digits for l1 (separated by spaces): ")
    l2_input = input("Enter digits for l2 (separated by spaces): ")
    l1_nums = [int(x) for x in l1_input.strip().split()]
    l2_nums = [int(x) for x in l2_input.strip().split()]
    l1 = createList(l1_nums)
    l2 = createList(l2_nums)
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print("Result linked list:")
    printList(result)