import unittest

# from Challenges.WarmUpChallenges.fibonacci import fibonacci_number
# from WarmUpChallenges.fibonacci import fibonacci_number
from fibonacci import fibonacci_number

class TestFibonacciNumber(unittest.TestCase):

    def test_large(self):
        for (n, Fn) in [(30, 832040), (35, 9227465), (40, 102334155)]:
            self.assertEqual(fibonacci_number(n), Fn)


if __name__ == '__main__':
    unittest.main()
