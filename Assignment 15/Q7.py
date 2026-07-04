def main():
    lst1 = []
    for i in range(100):
        a = input()
        
        if(a == "."):
            break
        
        lst1.append(a)

    Ret = list(filter(lambda x : len(x) >= 5, lst1))
    print(Ret)
    
if __name__ == "__main__":
    main()    