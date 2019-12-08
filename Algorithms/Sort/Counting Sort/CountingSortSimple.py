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

a=[list(map(int,input().split())) for _ in range(2)][1]
[print(i,a.count(i)) for i in set(a)]
