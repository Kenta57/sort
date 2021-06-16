from typing import List
import math

def merge_sort(A:List) -> List:
    n = len(A)

    if n == 1:
        return A

    mid_index = math.floor(n/2)
    R = merge_sort(A[:mid_index])
    L = merge_sort(A[mid_index:])

    l_index = 0
    r_index = 0
    len_R = len(R)
    len_L = len(L)

    M = []
    while l_index < len_R or r_index < len_L:
        if l_index == len_R:
            M.append(L[r_index])
            r_index += 1
        elif r_index == len_L:
            M.append(R[l_index])
            l_index += 1
        elif R[l_index] <= L[r_index]:
            M.append(R[l_index])
            l_index += 1
        elif R[l_index] > L[r_index]:
            M.append(L[r_index])
            r_index += 1

    return M



if __name__ == '__main__':
    l = [3,4,6,3,5,56,4,32,66,4]
    print(merge_sort(l))