def ChkPrime(no1):
    if no1 > 1:
        for i in range(2, no1):
            if no1 % i == 0:
                print("Not Prime Number")
                break
        else:
            print("Prime Number")
    else:
        print("Not Prime Number")    

def main():
    num = int(input("Enter a number: "))
    ChkPrime(num)

if __name__ == "__main__":
    main()    