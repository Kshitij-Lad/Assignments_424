def main():
    a = int(input("Enter a number: "))
    factorial = 1

    for i in range(1, a + 1):
        factorial *= i

    print(factorial)

if __name__ == "__main__":
    main()    