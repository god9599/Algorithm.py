import sys
import string

s = str(sys.stdin.readline())
alphabet = list(string.ascii_lowercase)

for i in alphabet:
    print(s.find(i), end = " ")