/*

BFS - LevelNodes

You have been given a Tree consisting of N nodes. A tree is a fully-connected graph consisting of N nodes and N-1 edges. The nodes in this tree are indexed from 1 to N. Consider node indexed 1 to be the root node of this tree. The root node lies at level one in the tree. You shall be given the tree and a single integer x . You need to find out the number of nodes lying on level x.

Input Format

The first line consists of a single integer N denoting the number of nodes in the tree. Each of the next n-1 lines consists of 2 integers a and b denoting an undirected edge between node a and node b. The next line consists of a single integer x.

Output Format

You need to print a single integers denoting the number of nodes on level x.

Constraints

Note
It is guaranteed that atleast one node shall lie on level x

SAMPLE INPUT 
20
11 1
1 2
13 3
15 4
17 5
11 6
2 7
1 8
15 9
4 10
15 12
5 13
2 14
17 15
15 16
11 17
15 18
9 19
16 20
2
SAMPLE OUTPUT 
3

*/

import java.util.*;

class Tree {
    private int V;
    private LinkedList<Integer> adj[];
    
    public Tree(int v) {
        V = v;
        adj = new LinkedList[v];
        for(int i=0; i<V; i++) {
            adj[i] = new LinkedList<Integer>();
        }
    }
    
    private void addEdge(int node1, int node2) {
        adj[node1].add(node2);
        adj[node2].add(node1);
    }
    
    private void nodeCount(int start, int value) {
        Queue<Integer> queue = new LinkedList<Integer>();
        boolean visited[] = new boolean[V];
        int level[] = new int[V];
        int parent;
        int count = 0;
        
        queue.add(start);
        level[start] = 0;
        visited[start] = true;
        while(!queue.isEmpty()) {
            parent = queue.poll();
            for(Integer curNode: adj[parent]) {
                if(!visited[curNode]) {
                    queue.add(curNode);
                    visited[curNode] = true;
                    level[curNode] = level[parent]+1;
                }
            }
        }
        for(int i=0; i<V; i++) {
            if(level[i] == value) {
                count++;
            }
        }
        System.out.println(count);
    }
    
    public static void main(String args[]) {
        int nodes, node1, node2, x;
        Scanner sc = new Scanner(System.in);
        nodes = sc.nextInt();
        Tree obj = new Tree(nodes);
        for (int i=0; i<nodes-1; i++) {
            node1 = sc.nextInt();
            node2 = sc.nextInt();
            obj.addEdge(node1-1,node2-1);
        }
        x = sc.nextInt();
        obj.nodeCount(0,x-1);
    }
}
