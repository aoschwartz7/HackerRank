# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem
    # If n = 5:
        # Return the value at index 5; f[5]
        # f = [0, 1, 1, 2, 3, 5, 8]
        # f[5] = 5 so return 5

    # n = 5

def fibonacci(n):

    # Base cases (conditions to end recursion):
    if n < 0:
        return 1
        
    if n <= 1:
        return n

    # Recursive case:
    else:
        return ((fibonacci(n-1) + fibonacci(n-2)))


if __name__ == '__main__':
    print(fibonacci(6)) # returns 8
