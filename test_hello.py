import unittest
from hello import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), "Hola, mundo!")

if __name__ == "__main__":
    unittest.main()
