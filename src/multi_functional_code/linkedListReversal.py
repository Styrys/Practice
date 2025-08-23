from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(nums):
    dummy = ListNode(0)
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def printList(node: Optional[ListNode]):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

if __name__ == "__main__":
    nums_input = input("Enter digits for the linked list (separated by spaces): ")
    nums = [int(x) for x in nums_input.strip().split()]
    head = createList(nums)
    reversed_head = reverseList(head)
    print("Reversed linked list:")
    printList(reversed_head)