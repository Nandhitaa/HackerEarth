/*
DFS - Unreachable Nodes

You have been given a graph consisting of N nodes and M edges. The nodes in this graph are enumerated from 1 to N . The graph can consist of self-loops as well as multiple edges. This graph consists of a special node called the head node. You need to consider this and the entry point of this graph. You need to find and print the number of nodes that are unreachable from this head node.

Input Format

The first line consists of a 2 integers N and M denoting the number of nodes and edges in this graph. The next M lines consist of 2 integers a and b denoting an undirected edge between node a and b. The next line consists of a single integer x denoting the index of the head node.

*Output Format *:

You need to print a single integer denoting the number of nodes that are unreachable from the given head node.

Constraints

SAMPLE INPUT 
10 10
8 1
8 3
7 4
7 5
2 6
10 7
2 8
10 9
2 10
5 10
2
SAMPLE OUTPUT 
0

*/

import java.util.*;

class Graph {
    private int V;
    private LinkedList<Integer> adj[];
    private int count;
    
    Graph(int v) {
        V =v;
        adj = new LinkedList[v];
        for(int i=0; i<V; i++) {
            adj[i] = new LinkedList();
        }
        count = 0;
    }
    
    void addEdge(int node1,int node2) {
        adj[node1].add(node2);
        adj[node2].add(node1);
    }
    
    void dfsUtil(int node, boolean visited[]) {
        visited[node] = true;
        count++;
        for(Integer neighbour: adj[node]) {
            if(!visited[neighbour]) {
                dfsUtil(neighbour, visited);
            }
        }
    }
    
    void dfs(int head) {
        boolean visited[] = new boolean[V];
        dfsUtil(head, visited);
        System.out.println(V-count);
    }
    
    public static void main(String args[]) {
        Scanner sc =new Scanner(System.in);
        int nodes = sc.nextInt();
        int edges = sc.nextInt();
        Graph graph = new Graph(nodes);
        for(int i=0; i<edges; i++) {
            graph.addEdge(sc.nextInt()-1, sc.nextInt()-1);
        }
        graph.dfs(sc.nextInt()-1);
    }
}
