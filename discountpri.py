amount = float(input("Enter the amount : "))
status = input("Is a Prime Member { Y for Yes } or {N for No} : ").upper()
isPrimeMem = False
if status == "Y":
    isPrimeMem = True

discount = 0

if amount >= 100000:
    discount = amount * 0.2 #20%
    print("20% Discount Applied : ",discount)
elif amount >= 50000:
    discount = amount * 0.1 #10%
    print("10% Discount Applied : ",discount)
elif amount >= 35000:
    discount = amount * 0.05 #5%
    print("5% Discount Applied : ",discount)
    
if isPrimeMem and amount > 0 :
    discount += amount * 0.05 #+5%
    print("Additional 5% Discount on Prime Member Applied Total Discount is : ",discount)
    
bill = amount - discount
    
print("The Bill amount is : ",bill)