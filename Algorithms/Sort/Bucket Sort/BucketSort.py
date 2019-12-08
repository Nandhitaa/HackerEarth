'''

You have been given an array A of size N. The array contains integers. You need to divide the elements of this array into buckets on the basis of the number of set bits in its binary representation. You need to then print the content of each bucket in a new line. The buckets should appear in the output in ascending order, i.e the bucket that stands for lesser number of set bits should appear before any other bucket which stands for higher number of set bits.The elements of each bucket should appear in ascending order too. That is if 2 integers appear in the same bucket, the one with the lower value should appear in the bucket list before the one with higher value.

Input Format:

The first line contains a single integer N denoting the size of the array. The next line contains N space separated integers denoting the elements of the array.

Output Format:

The output should contain the number of lines equal to the number of distnict bucket. If a bucket remains empty, it should not appear in the output. Print the contents of each bucket on a new line.

Constraints:



Note

It is guaranteed that each array element is unique.

SAMPLE INPUT 
5
1 2 3 4 5
SAMPLE OUTPUT 
1 2 4
3 5

'''

def insertion_sort(bucket):
    for i in range(len(bucket)):
        temp = bucket[i]
        j = i
        while j > 0 and temp < bucket[j-1]:
            bucket[j] = bucket[j-1]
            j = j - 1
        bucket[j] = temp

def bucket_sort(arr,bins):
    bucket = []
    for i in range(bins):
        bucket.append([])
    for x in arr:
        index = bin(x).count("1")
        bucket[index-1].append(x)
    for i in range(bins):
        insertion_sort(bucket[i])
        print(" ".join(map(str,bucket[i])))

if __name__ == '__main__':
    N = int(input())
    arr = [int(x) for x in input().split()]
    bins = 0
    for x in arr:
        bins = max(bins, bin(x).count("1"))
    bucket_sort(arr, bins)
