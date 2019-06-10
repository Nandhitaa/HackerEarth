def main():
    try:
        name = int(input())
        print(name * 2)
        name = input()
        print(name)
    except ValueError:
        print("Error")


main()