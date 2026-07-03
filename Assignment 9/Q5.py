def main():
    a = int(input())
    if(a % 3 == 0):
       if(a % 5 == 0):
           print("Divisible by 3 and 5")
       else:
           print("Only divisible by 3")
    else:
       if(a % 5 == 0):
           print("Only divisible by 5")  
       else:
           print("Not divisible by 3 and 5")
                                

if __name__ == "__main__":
    main()    