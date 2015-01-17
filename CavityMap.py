"""
David Schonberger
Hackerrank.com
Implementation - Cavity Map
1/12/2015
"""
n = input()
l = []
for i in range(n):
    row = raw_input()
    row = [int(x) for x in row]
    l.append(row)

if(n <= 2):
    for i in range(n):
        print ''.join(map(str,l[i]))

else:       
    cavity_list = []
    for i in range(1,n-1):
        for j in range(1,n-1):
            north = l[i][j] > l[i - 1][j]
            south = l[i][j] > l[i + 1][j]
            west = l[i][j] > l[i][j - 1]
            east = l[i][j] > l[i][j + 1]
            if(north and south and west and east):
                cavity_list.append([i,j])
                
    l = [map(str,elt) for elt in l]
    for i in range(n):
        cavs = [elt for elt in cavity_list if elt[0] == i]
        for elt in cavs:
            l[i][elt[1]] = 'X'
        print ''.join(map(str,l[i]))

#import numpy as np

#n = input()
#l = []
#for i in range(n):
#    row = raw_input()
#    #row = [c for c in row]
#    row = [int(x) for x in row]
#    l.append(row)
##print "l:",l
#
#if(n <= 2):
#    for i in range(n):
#        print ''.join(map(str,l[i]))
#else:       
#    arr = np.array(l)
#    cavity_list = []
#    for i in range(1,n-1):
#        for j in range(1,n-1):
#            north = l[i][j] > l[i - 1][j]
#            #north = arr[i,j] > arr[i-1,j]
#            south = l[i][j] > l[i + 1][j]
#            #south = arr[i,j] > arr[i+1,j]
#            west = l[i][j] > l[i][j - 1]
#            #west = arr[i,j] > arr[i,j-1]
#            east = l[i][j] > l[i][j + 1]
#            #east = arr[i,j] > arr[i,j+1]
#            if(north and south and west and east):
#                cavity_list.append([i,j])
#                
#    l = [map(str,elt) for elt in l]
#    for i in range(n):
#        cavs = [elt for elt in cavity_list if elt[0] == i]
#        for elt in cavs:
#            l[i][elt[1]] = 'X'
#        print ''.join(map(str,l[i]))
                
#    for i in range(n):
#        lst = list(arr[i,:])
#        lst = map(str,lst)
#        cavs = [elt for elt in cavity_list if elt[0] == i]
#        for elt in cavs:
#            lst[elt[1]] = 'X'
#        
#        print ''.join(map(str,lst))
