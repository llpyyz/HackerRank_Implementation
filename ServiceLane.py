"""
David Schonberger
Hackerrank.com
Implementation - Service lane
1/13/2015
"""

x = raw_input()
x = x.split(' ')
N = int(x[0])
T = int(x[1])
ar = raw_input()
ar = ar.split(' ')
ar = [int(t) for t in ar]

for i in range(T):
    indexes = raw_input()
    indexes = indexes.split(' ')
    indexes = [int(t) for t in indexes]
    print min(ar[indexes[0]:indexes[1] + 1])

