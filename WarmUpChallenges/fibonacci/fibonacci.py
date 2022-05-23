# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem

def fibonacci_number(n):

    # Base case:
    if n <= 1:
        return n
    
    fib_sequence = [0,1]

    for i in range(2,n+1):
        new = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(new)
    return fib_sequence[-1]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_number(n))
