import random as r
for i in range(1,11):
    a=r.randint(1,100)
    b=r.randint(1,100)
    print("Question",i,": ",a,"*",b)
    p=int(input("Enter Your answer "))
    if p==(a*b):
        print("Right!")
    else:
        print("Wrong. The answer is ",(a*b))
