from typing import List
import math

def swap(A:List, p:int, q:int) -> None:
    A[p], A[q] = A[q], A[p]

def getParent(n:int) -> int:
    return math.floor((n-1)/2)

def add_heap(A:List, i:int) -> None:
    while i != 0:
        p = getParent(i)
        if A[p] <= A[i]:
            swap(A,p,i)
            i = p
        else:
            break

def make_heap(A:List) -> None:
    n = len(A)
    for i in range(n):
        add_heap(A,i)

def remove_haep(A:List, e:int) -> None:
    s = 0
    swap(A,0,e)

    while 2*s + 1 < e:
        left = 2*s + 1
        right = 2*s + 2
        if A[s] >= A[left] and A[s] >= A[right]:
            break

        if A[left] < A[right]:
            if A[s] < A[right]:
                if right == e:
                    if A[s] < A[left]:
                        swap(A,s,left)
                        s = left
                    break
                swap(A,s,right)
                s = right
        else:
            if A[s] < A[left]:
                swap(A,s,left)
                s = left


def heap_sort(A:List) -> None:
    n = len(A)
    make_heap(A)
    for i in range(n)[::-1]:
        remove_haep(A,i)



if __name__ == '__main__':
    l = [3,4,6,3,5,56,4,32,66,4,-1]
    heap_sort(l)
    print(l)