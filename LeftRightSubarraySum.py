"""
David Schonberger
Hackerrank.com
Implementation - Left & right subarrays of equal sum
1/13/2015
"""
def subarray_sum(l):
    if(len(l) == 0):
        return 0
    else:
        return sum(l)

T = input()        
for i in range(T):
    n = input()
    ar = raw_input()
    ar = ar.split(' ')
    ar = [int(x) for x in ar]
    if(len(ar) == 1):
        print 'YES'
    elif(len(ar) == 2):
        print 'NO'
    else:
        res = 'NO'
        left_sum = ar[0]
        right_sum = sum(ar[2:])
        i = 1
        while(i < len(ar) - 1 and not left_sum == right_sum):
            left_sum += ar[i]
            right_sum -= ar[i+1]
            i += 1
        if(i < len(ar) - 1):
            res = 'YES'
        print res
