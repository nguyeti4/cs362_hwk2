#To run: python filename.py

def main():
    num = int(input("Enter a pos. int: "))
    if (num % 400) == 0 :
        print(str(num) + " is a leap year")
    else:
        if (num % 100) == 0:
            print(str(num) + " is not a leap year")
        else:
            if (num % 4) == 0:
                print(str(num) + " is a leap year")
            else:
                print(str(num) + " is not a leap year")

main()
