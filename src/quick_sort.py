from typing import List


'''
jでA[r]より大きいか小さいかを探す
もしA[r]より小さいものが見つかれば, iを更新し, そのindexにjのAを入れる
'''

def partition(A:List, p:int, r:int) -> int:
    # i : パーティション済のA[r]以下の末尾のindex
    i = p - 1
    for j in range(p,r):
        if A[j] <= A[r]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quick_sort(A:List, p:int, r:int) -> List:
    if p < r:
        i = partition(A,p,r)
        quick_sort(A,p,i-1)
        quick_sort(A,i+1,r)


if __name__ == '__main__':
    l = [3,4,6,3,5,56,4,32,66,4,-1,7,4,7]
    quick_sort(l,0,len(l)-1)
    print(l)