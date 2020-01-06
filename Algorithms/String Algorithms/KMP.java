/*
Knuth Morris Pratt Algorithm

Given 2 strings, P and T, find the number of occurrences of P in T.

Input:
First line contains string P, and second line contains the string T.

Output:
Print a single integer, the number of occurrences of P in T.

Constraints:

SAMPLE INPUT 
sda
sadasda
SAMPLE OUTPUT 
1

*/

import java.util.*;

class KMP {
    private String pattern;
    private String text;
    private int count;
    
    KMP(String pattern, String text) {
        this.pattern = pattern;
        this.text = text;
        count  = 0;
    }
    
    void applyKMP() {
        int textSize = text.length();
        int patternSize = pattern.length();
        int lps[] = new int[patternSize];
        createLPSArray(pattern, lps, patternSize);
        int j = 0;
        int i = 0;
        while(i<textSize) {
            if(pattern.charAt(j) == text.charAt(i)) {
                i++;
                j++;
            }
            else {
                if(j==0) {
                    i++;
                }
                else {
                    j = lps[j-1];
                }
            }
            if(j == patternSize) {
                count++;
                j = lps[j-1];
            }
        }
        System.out.println(count);
    }
    
    void createLPSArray(String pattern, int lps[], int size) {
        int len = 0;
        int i = 1;
        lps[0] = 0;
        while(i<size) {
            if(pattern.charAt(i) == pattern.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            }
            else {
                if(len == 0) {
                    lps[i] = len;
                    i++;
                }
                else {
                    len = lps[len-1];
                }
            }
        }
    }
    
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String pattern = sc.nextLine();
        String text = sc.nextLine();
        KMP kmp = new KMP(pattern, text);
        kmp.applyKMP();
    }
}