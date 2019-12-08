'''

Consider an Array a of size N
Iterate from 1 to N
In ith iteration select the ith minimum and swap it with a[i]
You are given an array a, size of the array N and an integer x. Follow the above algorithm and print the state of the array after x iterations have been performed.

Input Format

The first line contains two integer N and x denoting the size of the array and the steps of the above algorithm to be performed respectively. The next line contains N space separated integers denoting the elements of the array.

Output Format

Print N space separated integers denoting the state of the array after x steps

Constraints

SAMPLE INPUT 
5 2
5 4 2 3 1
SAMPLE OUTPUT 
1 2 4 3 5

'''

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def selection_sort(arr, iterations):
    for i in range(iterations):
        minimum = i
        for j in range(i+1, len(arr)):
            if (arr[j] < arr[minimum]):
                minimum = j
        swap(arr, i, minimum)

if __name__ == '__main__':
    N,x = map(int, input().split())
    arr = [int(x) for x in input().split()]
    
    selection_sort(arr, x)
    for i in range(N):
        print(arr[i], end=" ")
