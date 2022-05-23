import unittest
import numpy as np

from BubbleSort import countSwaps

class TestBubbleSort(unittest.TestCase):
    
    def test_large(self):
        np.random.seed(123)
        a = np.random.randint(100, size=(1000))
        self.assertEqual(countSwaps(a), 44751)


if __name__ == '__main__':
    unittest.main()