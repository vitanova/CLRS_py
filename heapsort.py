Parent = lambda i: int(i/2)
Left   = lambda i: 2*i
Right  = lambda i: 2*i +1

def max_heapify(A, i):
    l = Left(i)
    r = Right(i)
    n = len(A)
    if l <= n and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i
    if r <= n and A[r-1] > A[largest-1]:
        largest = r
    if largest != i:
        temp = A[i-1]
        A[i-1] = A[largest-1]
        A[largest-1] = temp
        max_heapify(A, largest)
        
def build_max_heap(A):
    n = len(A)
    for i in range(1, Parent(n)+1)[::-1]:
        max_heapify(A, i)

def heapsort(A):
    build_max_heap(A)
    n = len(A)
    A_s = [0]*n
    for i in range(1, n+1)[::-1]:
    	A_s[i-1] = A[1-1]
    	A[1-1]   = A[i-1]
    	A = A[:(i-1)]
    	max_heapify(A, 1)
    return A_s

A = [2, 8, 7, 1, 3, 5, 6, 4]
print(A)
A_s  = heapsort(A)
print(A_s)