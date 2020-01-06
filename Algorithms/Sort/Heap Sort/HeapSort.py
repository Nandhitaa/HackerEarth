'''

You are given a list of amount of money of T people, one by one. After each element in the list print the top 3 richest people's amount of money.

Input:
First line contains an integer, T, number of queries.
Next T lines contains an integer each, X.
ith query contains amount of money ith person have.

Output:
For each query, print the top 3 richest people's amount of money in the town and if there are less than 3 people in town then print -1.

Constraints:


SAMPLE INPUT 
5
1
2
3
4
5
SAMPLE OUTPUT 
-1
-1
3 2 1
4 3 2
5 4 3

'''

# Code without using class

import copy

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def min_heapify(arr, index, heap_size):
    left = 2*index + 1
    right = left + 1
    if left < heap_size and arr[left] < arr[index]:
        smallest = left
    else:
        smallest = index
    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right

    if smallest != index:
        swap(arr, smallest, index)
        min_heapify(arr, smallest, heap_size)

def build_min_heap(arr):
    for i in range(int(len(arr)/2), -1, -1):
        min_heapify(arr, i, len(arr))

def heap_sort(heap):
    sorted_arr = copy.deepcopy(heap)
    heap_size = len(heap)
    for i in range(len(sorted_arr)-1, 0, -1):
        swap(sorted_arr, 0, i)
        heap_size -= 1
        min_heapify(sorted_arr, 0, heap_size)
    return sorted_arr

def print_richest(sorted_arr):
    for element in sorted_arr:
        print(element, end=" ")
    print()

if __name__ == '__main__':
    T = int(input())
    k = 3
    arr = []
    sorted_arr = None
    for i in range(T):
        inp = int(input())
        if i < k-1:
            arr.append(inp)
            print(-1)
        elif i == k-1:
            arr.append(inp)
            build_min_heap(arr)
            sorted_arr = heap_sort(arr)
            print_richest(sorted_arr)
        else:
            if inp > arr[0]:
                arr[0] = inp
                min_heapify(arr, 0, len(arr))
                sorted_arr = heap_sort(arr)
                print_richest(sorted_arr)
            else:
                print_richest(sorted_arr)
