a=int(input("Enter the year "))
if a%4==0:
    if a%100!=0:
        print("The given year is Leap Year")
    else:
        if a%400==0:
            print("The given year is Leap Year")
        else:
            print("The given year is not a leap Year")
