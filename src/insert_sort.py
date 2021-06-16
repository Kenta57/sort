from typing import List

def insertSort(A : List) -> List:
    n = len(A)
    for i in range(n):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v

    return A

if __name__ == '__main__':
    l = [3,4,6,3,5,56,4,32,66,4,-1]
    l_s = insertSort(l)
    print(l_s)