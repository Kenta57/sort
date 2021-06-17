from typing import List

def countig_sort(A:List, k=100):
    B = [0] * (k+1)
    for a in A:
        B[a] += 1

    for i in range(1,k):
        B[i+1] = B[i] + B[i+1]

    C = [0] * len(A)
    for a in A[::-1]:
        C[B[a]-1] = a
        B[a] -= 1

    return C

if __name__ == '__main__':
    l = [12,4,5,4,4,5,12,8]
    print(countig_sort(l))

