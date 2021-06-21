from typing import List

def bucket_sort(A:List, k:int) -> List:
    for i in range(k)[::-1]:
        bucket = [[] for i in range(10)]
        for a in A:
            bucket[int(str(a).zfill(k)[i])].append(a)
        A = []
        for j in range(10):
            A += bucket[j]
    return A

if __name__ == '__main__':
    l = [34,70,13,555,55,21,89,41,3002]
    l = bucket_sort(l,4)
    print(l)