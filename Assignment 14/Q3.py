def main():
    a = int(input())
    b = int(input())

    MaxNum = lambda x,y : max(x,y)

    GreaterNum = MaxNum(a,b)
    print(GreaterNum)

if __name__ == "__main__":
    main()    