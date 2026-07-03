def ChkGreater(no1,no2):
    if(no1>no2):
        print(f"{no1} is greater")
    elif(no1 == no2):
        print("Both numbers are same")    
    else:
        print(f"{no2} is greater")    

def main():
    a = int(input())
    b = int(input())
    ChkGreater(a,b)

if __name__ == "__main__":
    main()    