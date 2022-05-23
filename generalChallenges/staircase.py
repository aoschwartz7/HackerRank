# https://www.hackerrank.com/challenges/staircase/problem

# Consider a staircase of size n = 4:

   #
  ##
 ###
####

# Observe that its base and height are both equal to n,
# and the image is drawn using # symbols and spaces.
# The last line is not preceded by any spaces.

# Write a program that prints a staircase of size n.

def staircase(n):
    space = ' '
    hash = '#'

    # create var x to serve as iterator
    x=n

    for i in range(n):
        print(space*(x-1) + hash*(i+1))
        # decrement spaces while incrementing hashes
        x -= 1

if __name__ == '__main__':
    staircase(4)
