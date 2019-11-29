'''
You have been given a sequence A of N digits. Each digit in this sequence ranges from 1 to  . You need to perform 2 types of operations on this list:

Add(x): Add element x to the end of the list.
Max(list): Find the maximum element in the current sequence.
For each query of type 2, you need to print the result of that operation.

Input Format

The first line consist of a single integer N denoting the size of the initial sequence. The next line consists of N space separated integers denoting the elements of the initial sequence. The next line contains a single integer q denoting the number of queries. The next q lines contains the details of the operation. The first integer type indicates the type of query. If typei ==1, it is followed by another integer x and you need to perform operation of type 1 else operations of type 2

Output Format

For each operation of the second type, print a single integer on a new line.

Constraints

SAMPLE INPUT
5
1 2 3 4 5
4
1 1
1 2
1 3
2
SAMPLE OUTPUT 
5

'''

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
class MaxHeap:
    def __init__(self, arr=[]):
        self.heap = arr
        self.build_maxheap()
    
    def heap_size(self):
        return len(self.heap) - 1

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def max_heapify(self, i):
        left = 2*i + 1
        right = left + 1
        N = self.heap_size()
        
        if (left <= N and self.heap[left] > self.heap[i]):
            largest = left
        else:
            largest = i
            
        if (right <= N and self.heap[right] > self.heap[largest]):
            largest = right
        
        if (largest != i):
            self.swap(i, largest)
            self.max_heapify(largest)
    
    def build_maxheap(self):
        N = self.heap_size()
        for i in range(int(N/2), -1, -1):
            self.max_heapify(i)
    
    def maximum(self):
        return self.heap[0]
    
    def insert_value(self, val):
        self.heap.append(val)
        self.shift_val()
    
    def shift_val(self):
        i = self.heap_size()
        while(i > 0 and self.heap[int(i/2)] < self.heap[i]):
            self.swap(int(i/2), i)
            i = int(i/2)
        
if __name__ == '__main__':
    N = int(input())
    heap = MaxHeap([int(x) for x in input().split()])
    t = int(input())
    for i in range(t):
        inp = input().split()
        if len(inp) > 1:
            heap.insert_value(int(inp[1]))
        else:
            print(heap.maximum())