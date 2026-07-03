def main():
    charc = input("Enter a character: ")

    if charc in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        print("Vowel")
    else:
        print("Consonant")

if __name__ == "__main__":
    main()    