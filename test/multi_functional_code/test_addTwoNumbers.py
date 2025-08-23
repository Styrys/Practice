import unittest
from src.multi_functional_code.addTwoNumbers import Solution, createList

def list_to_pylist(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        sol = Solution()
        l1 = createList([2,4,3])
        l2 = createList([5,6,4])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_pylist(result), [7,0,8])

        l1 = createList([0])
        l2 = createList([0])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_pylist(result), [0])

        l1 = createList([9,9,9,9,9,9,9])
        l2 = createList([9,9,9,9])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(list_to_pylist(result), [8,9,9,9,0,0,0,1])

if __name__ == "__main__":
    unittest.main()

