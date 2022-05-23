# https://www.hackerrank.com/challenges/compare-the-triplets/problem

# Alice and Bob each created one problem for HackerRank. A reviewer rates the
# two challenges, awarding points on a scale from 1 to 100  for three categories:
# problem clarity, originality, and difficulty.
# We define the rating for Alice's challenge to be the triplet:
#               a = (a[0], a[1], a[2])
# and the rating for Bob's challenge to be the triplet:
#               b = (b[0], b[1], b[2])

# Task it to find their comparison points by comparing a[0] with b[0], etc.
# if a[i] > b[i], alice gets 1 point
# if a[i] < b[i], bob gets 1 point
# if a[i] = b[i], neither get a point

# Output format: Return an array of two integers denoting the respective
#   comparison points earned by Alice and Bob.

def compareTriplets(a,b):
    aTotal = 0
    bTotal = 0
    x = 0
    for i in a:
        if a[x] > b[x]:
            aTotal += 1
        if a[x] < b[x]:
            bTotal += 1
        x += 1
    return aTotal, bTotal

if __name__ == '__main__':
    # below arrays should give output (1,2), ie Alice got 1 point and Bob 2
    a = [1,2,2]
    b = [2,3,1]
    print(compareTriplets(a,b))
