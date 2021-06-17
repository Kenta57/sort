from typing import List
from insert_sort import insert_sort

def generator() -> int:
    x = 1
    while True:
        yield x
        x = 3*x + 1

def make_G(n:int) -> List:
    a = generator()
    l = []
    v = next(a)
    while n > v:
        l.append(v)
        v = next(a)
    return l

def shell_sort(A:List) -> None:
    n = len(A)
    G = make_G(n)
    for g in G:
        insert_sort(A,g)


if __name__ == '__main__':
    l = [3,4,6,3,5,56,4,32,66,4,-1]
    shell_sort(l)
    print(l)
