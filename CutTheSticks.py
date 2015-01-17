"""
David Schonberger
Hackerrank.com
Implementation - Cut the sticks
1/13/2015
"""

n = input()
ar = raw_input()
ar = ar.split(' ')
ar = [int(x) for x in ar]
while(len(ar) > 0):
    num_sticks = len(ar)
    print num_sticks
    m = min(ar)
    ar = [x - m for x in ar]
    ar = [x for x in ar if x > 0]
    
