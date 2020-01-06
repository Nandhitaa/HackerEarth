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
# Code using class

import copy

class MinHeap:
    def __init__(self, arr=[]):
        self.heap = copy.deepcopy(arr)
        self.build_min_heap()
        self.sorted_arr = copy.deepcopy(self.heap)
        self.heap_sort()

    def heap_size(self):
        return len(self.heap) - 1

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def min_heapify(self, arr, index, N=None):
        left = 2*index + 1
        right = left + 1
        if N is None:
            N = self.heap_size()
        if left <= N and arr[left] < arr[index]:
            smallest = left
        else:
            smallest = index
        if right <= N and arr[right] < arr[smallest]:
            smallest = right
        if smallest != index:
            self.swap(arr, smallest, index)
            self.min_heapify(arr, smallest)

    def build_min_heap(self):
        N = self.heap_size()
        for i in range(int(N/2), -1, -1):
            self.min_heapify(self.heap, i)

    def minimum(self):
        return self.heap[0]

    def replace_minimum(self, val):
        self.heap[0] = val
        self.min_heapify(self.heap, 0)
        self.sorted_arr = copy.deepcopy(self.heap)
        self.heap_sort()

    def heap_sort(self):
        N = self.heap_size()
        for i in range(N, -1, -1):
            self.swap(self.sorted_arr, 0, i)
            N -= 1
            self.min_heapify(self.sorted_arr, 0, N)

    def richest(self):
        for element in self.sorted_arr:
            print(element, end=" ")
        print()

if __name__ == '__main__':
    T = int(input())
    k = 3
    arr = []
    for i in range(T):
        arr.append(int(input()))
        if i < k-1:
            print(-1)
        elif i == k-1:
            mh = MinHeap(arr)
            mh.richest()
        else:
            if arr[i] > mh.minimum():
                mh.replace_minimum(arr[i])
                mh.richest()
            else:
                mh.richest()
