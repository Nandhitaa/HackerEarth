'''

Given an array of N integers, you need to print the array after each pass of radix sort. In each pass, you need to sort the array by digits starting from least significant digit to most significant digit.

Input:
The first line consists of an integer N denoting the size of array.
The next line consists of N space separated integers.

Output:
Print the array after each pass. See the output for clarity.

Constraints:



SAMPLE INPUT 
8
170 45 75 90 802 24 2 66
SAMPLE OUTPUT 
170 90 802 2 24 45 75 66 
802 2 24 45 66 170 75 90 
2 24 45 66 75 90 170 802 

'''

def count_sort(arr, place):
    n = len(arr)
    num_range = 10
    count = [0] * num_range
    output = [0] * n
    for i in range(n):
        count[int((arr[i]/place)%num_range)] += 1
    for i in range(1,num_range):
        count[i] += count[i-1]
    for i in range(n-1,-1,-1):
        output[count[int((arr[i]/place)%num_range)]-1] = arr[i]
        count[int((arr[i]/place)%num_range)] -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr, maxx):
    place = 1
    while(maxx):
        count_sort(arr, place)
        print(" ".join(map(str,arr)))
        place*=10
        maxx = int(maxx/10)

if __name__ == '__main__':
    N = int(input())
    arr = [int(x) for x in input().split()]

    radix_sort(arr, max(arr))
