#import numpy as np
#%timeit quicksort(np.random.choice(20, 20, replace=False), 0, 19)

A = [2, 8, 7, 1, 3, 5, 6, 4]

def quicksort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
        
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp1 = A[i+1]
    A[i+1]= A[r]
    A[r]  = temp1
    #print(A, p, r, i+1)
    return i+1
print(A)
quicksort(A, 0, 7)
print(A)