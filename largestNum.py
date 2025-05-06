a = float(input("Enter the 1st Num :  "))
b = float(input("Enter the 2nd Num : "))
c = float(input("Enter the 3rd Num : "))

if a == b == c:
    print("All Numbers are Equal")
elif a > b and a > c:
    print("The Greatest Number is : ",a)
elif b > a and b > c:
    print("The Greatest Number is : ",b)
else:
    print("The Greatest Number is : ",c)