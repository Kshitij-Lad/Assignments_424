def main():
    a = int(input("Enter a number: "))

    original = a
    reverse = 0

    while a > 0:
        digit = a % 10
        reverse = reverse * 10 + digit
        a //= 10

    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()    