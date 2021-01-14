
def validateEmail():
    email = input("Enter Email id: ")
    result = email.find("@")
    if(result != -1):
        print("Valid Email")
    else:
        print("Invalid Email")


validateEmail()
