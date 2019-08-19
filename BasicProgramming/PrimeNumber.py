'''
You are given an integer N. You need to print the series of all prime numbers till N.
Input Format
The first and only line of the input contains a single integer N denoting the number till where you need to find the series of prime number.
Output Format
Print the desired output in single line separated by spaces.
Constraints
1<=N<=1000
'''


def main():
    val = int(input())
    if val == 0:
        print("")
    elif val == 1:
        print("")
    else:
        for i in range(2, val + 1):
            j = 2
            while j <= i:
                if j == i:
                    print(i, end=" ")
                if i % j == 0:
                    break
                else:
                    j = j + 1


main()