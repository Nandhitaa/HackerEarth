'''

You have been given an A array consisting of N integers. All the elements in this array are guaranteed to be unique. For each position i in the array A you need to find the position A[i] should be present in, if the array was a sorted array. You need to find this for each i and print the resulting solution.

Input Format:

The first line contains a single integer N denoting the size of array A. The next line contains N space separated integers denoting the elements of array A.

Output Format:

Print N space separated integers on a single line , where the Ith integer denotes the position of A[i] if this array were sorted.

Constraints:


SAMPLE INPUT 
5
1 2 3 4 5
SAMPLE OUTPUT 
1 2 3 4 5

'''

import copy

def insertion_sort(arr):
    unsorted_arr = copy.deepcopy(arr)
    for i in range(len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = temp
    
    print(" ".join(map(lambda x: str(arr.index(x)+1), unsorted_arr)))

if __name__ == '__main__':
    N = int(input())
    arr = [int(x) for x in input().split()]
    
    insertion_sort(arr)
