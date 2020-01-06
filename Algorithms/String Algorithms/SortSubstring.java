/*

Given a string S, and two numbers N, M - arrange the characters of string in between the indexes N and M (both inclusive) in descending order. (Indexing starts from 0).

Input Format:
First line contains T - number of test cases.
Next T lines contains a string(S) and two numbers(N, M) separated by spaces.

Output Format:
Print the modified string for each test case in new line.

Constraints:

SAMPLE INPUT 
3
hlleo 1 3
ooneefspd 0 8
effort 1 4

SAMPLE OUTPUT 
hlleo
spoonfeed
erofft

*/

import java.util.*;
import java.lang.*;

class SortSubstring {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int i=0; i<T; i++) {
            String s = sc.next();
            int start = sc.nextInt();
            int end = sc.nextInt();
            
            String substring = s.substring(start,end+1);
            char[] ch = substring.toCharArray();
            Arrays.sort(ch);
            String reverse = new StringBuilder(String.valueOf(ch)).reverse().toString();
            System.out.println(s.substring(0,start)+reverse+s.substring(end+1,s.length()));
        }
    }
}