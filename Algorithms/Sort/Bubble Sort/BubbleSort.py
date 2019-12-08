'''

You have been given an array A of size N . you need to sort this array non-decreasing oder using bubble sort. However, you do not need to print the sorted array . You just need to print the number of swaps required to sort this array using bubble sort

Input Format

The first line consists of a single integer N denoting size of the array. The next line contains N space separated integers denoting the elements of the array.

Output Format Print the required answer in a single line

Constrains 


SAMPLE INPUT 
5
1 2 3 4 5
SAMPLE OUTPUT 
0

'''

if __name__ == '__main__':
    N = int(input())
    elements = [int(x) for x in input().split()]

    swap_count = 0

    for k in range(N-1):
        for i in range(N-k-1):
            if (elements[i] > elements[i+1]):
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
                swap_count = swap_count + 1

    print(swap_count)
