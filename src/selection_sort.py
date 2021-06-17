from typing import List

def selection_sort(A:List) -> None:
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i,n):
            if A[min_index] > A[j]:
                min_index = j
        A[min_index], A[i] = A[i], A[min_index]

if __name__ == '__main__':
    l = [3,4,6,3,5,56,4,32,66,4,-1]
    selection_sort(l)
    print(l)