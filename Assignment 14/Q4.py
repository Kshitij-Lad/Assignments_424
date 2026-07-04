def main():
    a = int(input())
    b = int(input())

    MinNum = lambda x,y : min(x,y)

    SmallerNum = MinNum(a,b)
    print(SmallerNum)

if __name__ == "__main__":
    main()    