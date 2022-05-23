""" Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm below. 
Once sorted, print the following three lines:

for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }
    
} """

# import random
import numpy as np
from typing import List

# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.


def countSwaps(a:List[int]) -> int:
    num_swaps = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                num_swaps += 1
    return num_swaps


if __name__ == '__main__':
    np.random.seed(123)
    a = np.random.randint(100, size=(1000))
    # a = [6,4,1]
    num_swaps = countSwaps(a)
    print(num_swaps)
    