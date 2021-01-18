
def validateEmail():
    email = input("Enter Email id: ")
    result = email.find("@")
    if((result == -1) or email.startswith("@")):
        print("Invalid Email")
    else:
        print("Valid Email")


validateEmail()
