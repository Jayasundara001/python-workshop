name1=int (input("Enter your number"))
name2=int (input("Enter your number"))
name3=int (input("Enter your number"))

if(name1>name2):
    if(name1>name3):
     print(name1)
    else:
        print(name2)
else:
    if(name2>name3):
     print(name2)
    else:
      print(name3)