from typing import List

def insert_sort(A : List, g=1) -> List:
    n = len(A)
    for i in range(g,n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
        A[j+g] = v

    return A

def insert_sort_base(A : List) -> List:
    n = len(A)
    for i in range(1,n):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v

    return A

if __name__ == '__main__':
    l = [3,4,6,3,5,56,4,32,66,4,-1]
    l = list(range(10)[::-1])
    print(l)
    l_s = insert_sort(l,3)
    print(l_s)