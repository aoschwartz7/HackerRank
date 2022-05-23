# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# see above link for challenge description

def hourGlassCounter(ar, row, col):

    # Define hourglass shape
    a = ar[row][col]
    b = ar[row][col+1]
    c = ar[row][col+2]
    d = ar[row+1][col+1]
    e = ar[row+2][col]
    f = ar[row+2][col+1]
    g = ar[row+2][col+2]


    return (a+b+c+d+e+f+g)

if __name__ == '__main__':
    ar = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
        ]
    maxx = -1
    # Create nested for loops that index into array matrix
    for row in range(len(ar)-2):
        for col in range(len(ar)-2):
            # Create sum of each hourglass
            summ = hourGlassCounter(ar, row, col)
            # Keep track of greatest sum hourglass
            if summ > maxx:
                maxx = summ
    print(maxx)
