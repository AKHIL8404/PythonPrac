n = False

if isinstance(n,bool):
    print("It is a Boolean Value")
elif isinstance(n,int):
    print("It is a Number")
elif isinstance(n,str):
    print("It is a Text")
elif isinstance(n,float):
    print("It is a Float Value")
else:
    print("It may be Iterators or UserDifined Type")
