def greeting (name):
    message=f"hello ,{name}"
    return message

print(greeting("afrin"))

def checkEven():
    for i in range(1,20):
        if i%2==0:
            pass
            #print(f"{i} is even")
        else:
            print(f"{i} is odd")

print(checkEven())

def num():
    for i in range(10):
        if i==5:
            break
        else:
            print(i)
num()
