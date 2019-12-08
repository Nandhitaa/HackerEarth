'''

You have been given an integer array A of size N. Each element of the array ranges between 1 and 10^5. You need to find the frequency of each distinct element of the array. The elements need to be present in the output in ascending order. You need to print the value and then frequency of each distinct element.

Input Format:

The first line contains a single integer N denoting the size of the array. The next line contains N space separated integers, denoting the elements of the array.

Output Format

For each distinct integer, print its value and then frequency in a new line. The distinct integers should appear in the output in ascending order.

Constraints



SAMPLE INPUT 
5
5 4 3 2 1
SAMPLE OUTPUT 
1 1
2 1
3 1
4 1
5 1

'''

def counting_sort(arr):
    K = max(arr)
    aux = [0] * (K+1)
    for i in range(len(arr)):
        aux[arr[i]]+= 1
    [print(i,aux[i]) for i in range(K+1) if aux[i] != 0]

if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]
    counting_sort(A)
