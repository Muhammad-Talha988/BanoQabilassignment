again="yes"
while again=="yes":
  a=int(input("enter a number"))
  sign=(input("enter sign +-*/"))
  b=int(input("enter a number"))
  if sign=="+":
    print(a+b)
  elif sign=="-":
    print(a-b)
  elif sign=="*":
       print(a*b)
  elif sign=="/":
        if b==0:
          print("error")
        else:
          print(a/b)
  else:
      print("invalid sign")
  again=input("do you want to continue yes/no  ")