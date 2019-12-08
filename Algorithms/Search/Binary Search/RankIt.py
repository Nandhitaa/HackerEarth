'''
You have been given an array A consisting of N integers. All the elements in this array A are unique. You have to answer some queries based on the elements of this array. Each query will consist of a single integer x. You need to print the rank based position of this element in this array considering that the array is 1 indexed. The rank based position of an element in an array is its position in the array when the array has been sorted in ascending order.

Note: It is guaranteed that all the elements in this array are unique and for each x belonging to a query, value x shall exist in the array

Input Format

The first line consists of a single integer N denoting the size of array A. The next line contains N unique integers, denoting the content of array A. The next line contains a single integer q denoting the number of queries. Each of the next q lines contains a single integer x denoting the element whose rank based position needs to be printed.

Output Format

You need to print q integers denoting the answer to each query.

Constraints

SAMPLE INPUT 
5
1 2 3 4 5
5
1
2
3
4
5
SAMPLE OUTPUT 
1
2
3
4
5

'''

class BinarySearch:
    def __init__(self, array=[]):
        self.arr = array
        self.arr.sort()
    
    def search(self, key, low=0, high=None):
        if high is None:
            high = len(self.arr) - 1

        if (low > high):
            return -1

        mid = int((low + high)/2)

        if (key < self.arr[mid]):
            high = mid - 1
            return self.search(key, low, high)
        elif (key > self.arr[mid]):
            low = mid + 1
            return self.search(key, low, high)
        else:
            return mid + 1
    
if __name__ == '__main__':
    size = int(input())
    arr = [int(x) for x in input().split()]
    obj = BinarySearch(arr)
    queries = int(input())
    for i in range(0,queries):
        print(obj.search(int(input())))
