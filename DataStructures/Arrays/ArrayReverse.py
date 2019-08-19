'''
Print Array in Reverse

Given the size and the elements of array A, print all the elements in reverse order.

Input: 
First line of input contains, N - size of the array. 
Following N lines, each contains one integer, i{th} element of the array i.e. A[i].

Output: 
Print all the elements of the array in reverse order, each element in a new line.

Constraints:

SAMPLE INPUT 
5
4
12
7
15
9
SAMPLE OUTPUT 
9
15
7
12
4

'''

N = int(input())
arr = []
for i in range(N):
    x = int(input())
    arr.append(x)

for i in range(N):
    print(arr[N-i-1])