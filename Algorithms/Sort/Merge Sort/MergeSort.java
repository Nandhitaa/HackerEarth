/*

Given an array A on size N, you need to find the number of ordered pairs (i,j) such that i < j and A[i] > A[j].

Input:
First line contains one integer, N, size of array.
Second line contains N space separated integers denoting the elements of the array A.

Output:
Print the number of ordered pairs (i,j) such that i < j and A[i] > A[j].

Constraints:


SAMPLE INPUT 
5
1 4 3 2 5
SAMPLE OUTPUT 
3

*/

import java.util.*;

class TestClass {

    static long count = 0;

    private static void merge(int arr[], int start, int mid, int end) {
        int p = start;
        int q = mid + 1;
        int length = end-start+1;
        int sortedArr[] = new int[length];
        for (int i=0; i<length; i++) {
            if(p>mid) {
                sortedArr[i] = arr[q++];
            }
            else if(q>end) {
                sortedArr[i] = arr[p++];
            }
            else if (arr[p] <= arr[q]) {
                sortedArr[i] = arr[p++];
            }
            else {
                sortedArr[i] = arr[q++];
                count = count + mid - p + 1;
            }
        }

        for (int k=0; k<length; k++) {
            arr[start++] = sortedArr[k];
        }
    }

    private static void mergeSort(int arr[], int start, int end) {
        if (start < end) {
            int mid = (start+end)/2;
            mergeSort(arr,start,mid);
            mergeSort(arr,mid+1,end);
            merge(arr,start,mid,end);
        }
    }

    public static void main(String args[] ) throws Exception {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int A[] = new int[n];
        for(int i=0; i<n; i++) {
            A[i] = s.nextInt();
        }
        mergeSort(A, 0, n-1);
        System.out.println(count);
    }
}
