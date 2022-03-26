# Aleksandar Lukic 

# This is an alogrithm to find a peak inside an array.
# It has logarithmic running time, f(n) = O(log n)

# Test input for terminal. Copy and paste these numbers:
""" 
8
5 7 7 8 13 13 12 1
"""

def find_peak_logarithmic(arr, left_p, right_p):
    # If array has a sinlge element
    if left_p == right_p:
        return left_p
    # Find middle pointer
    mid_p = (left_p + right_p) // 2    
    
    # If peak inside array 
    if(arr[mid_p - 1] <= arr[mid_p] and arr[mid_p] >= arr[mid_p + 1]):
        return mid_p
    # Recursive calls
    elif(arr[mid_p - 1] >= arr[mid_p]):
        return find_peak_logarithmic(arr, left_p, mid_p - 1)
    elif(arr[mid_p] <= arr[mid_p + 1]):
        return find_peak_logarithmic(arr, mid_p + 1, right_p)

# Reading user input from terminal
n = int(input())
A = [int(x) for x in input().split()]

# Print to terminal
print(find_peak_logarithmic(A, 0, len(A)-1))
