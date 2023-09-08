import unittest

def hello_world():
    return 'Hello, world!'

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_output(self):
        result = hello_world()
        self.assertEqual(result, 'Hello, world!')

if __name__ == '__main__':
    unittest.main()
