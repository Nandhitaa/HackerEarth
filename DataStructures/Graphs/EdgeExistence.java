/*

You have been given an undirected graph consisting of N nodes and M edges. This graph can consist of self-loops as well as multiple edges. In addition , you have also been given Q queries. For each query , you shall be given 2 integers A and B. You just need to find if there exists an edge between node A and node B. If yes, print "YES" (without quotes) else , print "NO"(without quotes).

Input Format:

The first line consist of 2 integers N and M denoting the number of nodes and edges respectively. Each of the next M lines consist of 2 integers A and B denoting an undirected edge between node A and B. The next line contains a single integer Q denoting the number of queries. The next Line contains 2 integers A and B denoting the details of the query.

Output Format

Print Q lines, the answer to each query on a new line.

Constraints:

*/

import java.util.*;

class EdgeExistence {
    public static void main(String args[] ) throws Exception {
        Scanner sc = new Scanner(System.in);
        int nodes = sc.nextInt();
        int edges = sc.nextInt();
        int adjacencyMatrix[][] = new int[nodes][nodes];
        int start,end;
        for(int i=0; i<edges; i++) {
            start = sc.nextInt();
            end = sc.nextInt();
            adjacencyMatrix[start-1][end-1] = 1;
            adjacencyMatrix[end-1][start-1] = 1;
        }
        int queries = sc.nextInt();
        for(int i=0; i<queries; i++) {
            start = sc.nextInt();
            end = sc.nextInt();
            if(start<nodes && end<nodes && adjacencyMatrix[start-1][end-1] == 1) {
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
            }
        }
        sc.close();
    }
}
