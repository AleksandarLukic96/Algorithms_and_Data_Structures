# Aleksandar Lukic 

# These are two alogrithms to find a peak inside an array.
# They have linear running time, f(n) = O(n)

# Note: Since the two algorithms are implemented differently,
# they may spit out different values.
# However, these values will still be valid, 
# as there can be multiple peaks in an array.

# Test input for terminal. Copy and paste these numbers:
""" 
8
5 7 7 8 13 13 12 1
"""

def find_peak_1(a):
    n = len(a)
    if(a[0] >= a[1]):
        return 0
    for i in range(1, n-1):
        if(a[i-1] <= a[i] and a[i] >= a[i+1]):
            return i
    if(a[n-2] <= a[n-1]):
        return n-1
    
def find_peak_2(a):
    n = len(a)
    max = 0
    for i in range(n):
        if(a[i] > a[max]):
            max = i
    return max

# Reading user input from terminal
n = int(input())
A = [int(x) for x in input().split()]

# Print to terminal
print(find_peak_1(A))
print(find_peak_2(A))