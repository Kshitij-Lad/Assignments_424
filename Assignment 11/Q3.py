def main():
    a = int(input("Enter a number: "))
    sum = 0

    while a > 0:
        digit = a % 10
        sum += digit
        num //= 10

    print(sum)
if __name__ == "__main__":
    main()    