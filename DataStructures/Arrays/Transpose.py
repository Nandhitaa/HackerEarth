'''
Transpose

Given a 2D array A, your task is to convert all rows to columns and columns to rows.

Input: 
First line contains 2 space separated integers, N - total rows, M - total columns. 
Each of the next N lines will contain M space separated integers.

Output: 
Print M lines each containing N space separated integers.

Constraints:

SAMPLE INPUT 
3 5
13 4 8 14 1
9 6 3 7 21
5 12 17 9 3
SAMPLE OUTPUT 
13 9 5
4 6 12
8 3 17
14 7 9
1 21 3

'''

N,M = [int(x) for x in input().split()]
arr = []
for i in range(N):
    t = input()
    arr.append([int(x) for x in t.split()])

for j in range(M):
    for i in range(N):
        print(arr[i][j], end=" ")
    print()