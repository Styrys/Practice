import unittest
from src.multi_functional_code.linkedListReversal import createList, reverseList

def list_to_pylist(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

class TestLinkedListReversal(unittest.TestCase):
    def test_reverse_list(self):
        head = createList([1,2,3,4,5])
        reversed_head = reverseList(head)
        self.assertEqual(list_to_pylist(reversed_head), [5,4,3,2,1])

        head = createList([])
        reversed_head = reverseList(head)
        self.assertEqual(list_to_pylist(reversed_head), [])

        head = createList([42])
        reversed_head = reverseList(head)
        self.assertEqual(list_to_pylist(reversed_head), [42])

if __name__ == "__main__":
    unittest.main()

