'''

Given an array A on size N, you need to find the number of ordered pairs (i,j) such that i < j and A[i] > A[j].

Input:
First line contains one integer, N, size of array.
Second line contains N space separated integers denoting the elements of the array A.

Output:
Print the number of ordered pairs (i,j) such that i < j and A[i] > A[j].

Constraints:


SAMPLE INPUT 
5
1 4 3 2 5
SAMPLE OUTPUT 
3

'''

count = 0

def merge(arr, start, mid, end):
    global count
    p=start
    q=mid+1
    sorted_arr = []
    for _ in range(end-start+1):
        if p > mid:
            sorted_arr.append(arr[q])
            q=q+1
        elif q > end:
            sorted_arr.append(arr[p])
            p=p+1
        elif arr[p] <= arr[q]:
            sorted_arr.append(arr[p])
            p=p+1
        else:
            sorted_arr.append(arr[q])
            q=q+1
            count = count + mid - p + 1
    for i in range(len(sorted_arr)):
        arr[start] = sorted_arr[i]
        start=start+1

def merge_sort(arr, start, end):
    if start < end:
        mid = int((start + end)/2)
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)

if __name__ == '__main__':
    global count
    N = int(input())
    A = [int(x) for x in input().split()]

    merge_sort(A, 0, N-1)
    print(count)
