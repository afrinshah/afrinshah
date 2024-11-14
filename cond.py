name=input("enter username for login:")
password=input("enter password:")
if(name=="afrin" and password=="afrinshah"):
    print(f"welcome {name} to diya application")
else:
    print("invalid")


n=int(input("enter the number:"))
if n==0:
    print("it is not zero")
elif n>10:
    print("greater")
elif n<10:
    print("smaller")
else:
    print("please try again")


           
#x=int(input("enter the number:"))
#if(x%2)==0:
 #   print(f"{x} is even")
#else:
 #   print("{x} is odd")

#for a in range(1,10):

  #  if a %2==0:
        #print(f"{a} is even")
  #  else:
      #  print(f"{a} is odd")
        


num = 55

if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
            print(num, "is a prime number")
else:
    print(num, "is not a prime number") 
