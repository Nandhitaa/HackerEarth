'''

You are given container full of water. Container can have limited amount of water. You also have N bottles to fill. You need to find the maximum numbers of bottles you can fill.

Input:
First line contains one integer, T, number of test cases.
First line of each test case contains two integer, N and X, number of bottles and capacity of the container.
Second line of each test case contains N space separated integers, capacities of bottles.

Output:
For each test case print the maximum number of bottles you can fill.

Constraints:

SAMPLE INPUT 
1
5 10
8 5 4 3 2
SAMPLE OUTPUT 
3

'''

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        bottles, container = [int(x) for x in input().split()]
        capacities = [int(x) for x in input().split()]
        capacities.sort()
        total = 0
        count = 0
        for i in range(bottles):
            container -= capacities[i]
            if container >= 0:
                count += 1
        print(count)
