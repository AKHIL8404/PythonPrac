a = float(input("Enter the 1st Num :  "))
b = float(input("Enter the 2nd Num : "))
c = float(input("Enter the 3rd Num : "))

if a > b and a > c:
    print("Greatest Number is : ",a)
elif b > a and b > c:
    print("Greatest Number is : ",b)
else:
    print("Greatest Number is : ",c)