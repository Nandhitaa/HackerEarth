'''

You have been given an Unimodal function:
f(x) = 2 * x * x - 12 * x + 7

with N intervals. For each interval you will be given two integer values l and r , where l<=r and you need to find the minimum value of f(x) where x will be in the range [l,r] (both inclusive).

Input:
The first line will consists of one integer N denoting the number of intervals.
In next N lines, each line contains 2 space separated integers, l and r denoting the range of interval.

Output:
Print N lines, where ith line denotes the minimum value of f(x), where x will be in range [li,ri]
.

Constraints:


SAMPLE INPUT 
1
6 8
SAMPLE OUTPUT 
7

'''

def func(x):
    return x * (x - 6)

def mino(l,r):
    if (l<3 and r >3):
        return -11
    for _ in range(60):
        mid1 = l + (r-l)/3
        mid2 = r - (r-l)/3
        if (func(mid1) < func(mid2)):
            r = mid2
        else:
            l = mid1
    return round(2 * func(l) + 7)

if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        l,r = map(float, input().split())
        print(mino(l,r))