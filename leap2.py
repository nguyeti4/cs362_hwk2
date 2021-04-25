#To run: python leap2.py
def main():
    string = input("Enter a pos. int: ")
    if(string.isdigit()==True):
        num = int(string)
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
    else:
        if(string[0]=='-'):
            print("error: input needs to be a POSITIVE int")
        else:
            print("error: input needs to be an INT")
main()
