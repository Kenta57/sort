from typing import List

def bubble_sort(A : List) -> None:
    n = len(A)
    flag = True
    while flag:
        flag = False
        for i in range(n-1,0,-1):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                flag = True

if __name__ == '__main__':
    l = [3,4,6,3,5,56,4,32,66,4,-1]
    bubble_sort(l)
    print(l)