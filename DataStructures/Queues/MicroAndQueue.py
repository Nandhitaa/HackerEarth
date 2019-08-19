'''
Micro just purchased a queue and wants to perform N operations on the queue. The operations are of following type:

 : Enqueue x in the queue and print the new size of the queue.
D : Dequeue from the queue and print the element that is deleted and the new size of the queue separated by space. If there is no element in the queue then print 1 in place of deleted element.

Since Micro is new with queue data structure, he need your help.

Input:
First line consists of a single integer denoting N
Each of the following N lines contain one of the operation as described above.

Output:
For each enqueue operation print the new size of the queue. And for each dequeue operation print two integers, deleted element (1, if queue is empty) and the new size of the queue.

Constraints:


SAMPLE INPUT 
5
E 2
D
D
E 3
D
SAMPLE OUTPUT 
1
2 0
-1 0
1
3 0
'''

class Queue:
    
    def __init__(self,capacity):
        self.queue = [None] * capacity
        self.size = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self,x):
        if not self.isFull():
            self.queue[self.rear] = x
            self.rear = (self.rear + 1) % self.capacity
            self.size = self.size + 1
            print(self.size)

    def dequeue(self):
        if not self.isEmpty():
            self.size = self.size - 1
            print(self.queue[self.front], self.size)
            self.front = (self.front + 1) % self.capacity
        else:
            print(-1, self.size)

if __name__ == '__main__':
    q = Queue(100)
    N = int(input())
    for i in range(N):
        inp = input()
        if inp[0] == 'E':
            q.enqueue(inp.split()[1])
        elif inp[0] == 'D':
            q.dequeue()
