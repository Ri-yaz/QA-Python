def check(number):
    if number%2==0:
        print("Given number is even")
    else:
        print("Given number is odd")
number=int(input("Enter a number : "))
check(number)


def validate_login(username, password):
    if username == "admin" and password == "1234":
        return True
    return False
result = validate_login("admin", "1234")
print("Login successful:", result)
    
