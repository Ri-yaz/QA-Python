#def function():
   # print("hello world")

#function()
#function()
#function()

def greet(name):
    print("hello",name)
    print("good morning", name)
    print("good afternoon", name)
    print("good evening", name)
greet("riyaz")


def sum(x,y):
    return x+y
result=sum(2,3)
if result>10:
    print("Greater than 10.")
else:
    print("lESS than 10.")


'''def user_info():
    name=input("Enter your name")
    lname=input("Enter your name")
    fullname= name + lname
    print(fullname)
#user_info()
'''

def greet(name="student"):
    print("heloo",name)
greet()
greet("riyaz")
