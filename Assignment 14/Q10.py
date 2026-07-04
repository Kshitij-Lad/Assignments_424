def main():
    a = int(input())
    b = int(input())
    c = int(input())

    MaxNum = lambda x,y,z : max(x,y,z)

    GreaterNum = MaxNum(a,b,c)
    print(GreaterNum)

if __name__ == "__main__":
    main()    