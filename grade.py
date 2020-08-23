print("Enter the maarks obtained in the following subject out of 100")
maths = eval(input("Enter the marks obtained in maths"))
phy = eval(input("Enter the marks obtained in physics"))
chem = eval(input("Enter the marks obtained in chemistry"))
eng = eval(input("Enter the marks obtained in english"))
ss = eval(input("Enter the marks obtained in Social Studies"))
p = (( maths + phy + chem + eng + ss )/500) * 100
print('The percentage obtained is')
print(p)
if(p>=90):
    print('You got 1st class marks')
if((p>=70) and (p<90)):
    print('You got 2nd class marks')
if((p>=60) and (p<70)):
    print('You have just passed')
if(p<60):
    print('Sorry you have failed')
