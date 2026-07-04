
def main():
    lst1 = []
    for i in range(100):
        a = input()
        
        if(a == "."):
            break
        
        lst1.append(int(a))

    Ret = list(map(lambda x: x*x, lst1))
    print(Ret)
    
if __name__ == "__main__":
    main()    