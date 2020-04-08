# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#
# Lilah has a string, s, of lowercase English letters that she repeated
# infinitely many times. Given an integer, n, find and print the number of
# letter a's in the first n letters of Lilah's infinite string.
#
# For example, if the string s ='abcac' and n = 10, the substring we consider is
# 'abcacabcac', the first 10 characters of her infinite string. There are 4
# occurrences of a in the substring.
#
# Function Description
# Function should return an integer representing the number of occurrences of a
# in the prefix of length n in the infinitely repeating string.
#
# repeatedString has the following parameter(s):
#
# s: a string to repeat
# n: the number of characters to consider

def repeatedString(s,n):
    newString = ''
    a = 0

# 1) create new string
    while (len(newString) < n):
        # add first element in original string to new string
        for x in s:
            newString = newString + x

    # 2) count a's
    for l in newString:
        if l == 'a':
            a += 1
    return a

if __name__ == '__main__':
    print(repeatedString('abcac', 10))
