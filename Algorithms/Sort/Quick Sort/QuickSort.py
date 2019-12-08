'''

You have been given an array A of size N.This array contains integers ranging from 1 to 1o^9. You need to sort the contents of this array by their value and then print the contents of it.

Input Format:

The first line contains a single integers N denoting the size of the array. The next line contains N space separated integers denoting the contents of the array.

Output Format:

Print N space separated integers, i.e. the final sorted array.

Constraints:



SAMPLE INPUT 
5
4 3 1 5 2
SAMPLE OUTPUT 
1 2 3 4 5

'''

def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    for j in range(start+1, end+1):
        if arr[j] < pivot:
            swap(arr,i,j)
            i = i + 1
    swap(arr, start, i-1)
    return i-1

def quick_sort(arr, start, end):
    if start < end:
        pivot_pos = partition(arr,start,end)
        quick_sort(arr, start, pivot_pos-1)
        quick_sort(arr, pivot_pos+1, end)

if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    quick_sort(A, 0, N-1)
    print(" ".join(map(str, A)))
