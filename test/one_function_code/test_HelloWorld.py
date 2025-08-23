import unittest
from src.one_function_code.HelloWorld import HelloWorld

class TestHelloWorld(unittest.TestCase):
    def test_greet(self):
        hello = HelloWorld()
        self.assertEqual(hello.greet(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()

