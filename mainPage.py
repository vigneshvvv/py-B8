users = [
    {
        "userName": "Sathish",
        "password": "Sathish"
    },
    {
        "userName": "Vignesh",
        "password":"Vignesh@123"
    },
    {
        "userName": "Deva",
        "password": "Deva@321"
    }
]

def loginUser():
    global users
    attempts = 1

    while attempts <= 4:
        if attempts == 4:
            print("Maximum attempts reached. please try again after sometime")
            break

        userN = input("Enter your userName: ")
        passN = input("Enter your password: ")

        isLogin = False
        for user in users:
            if user["userName"] == userN and user["password"] == passN:
                isLogin = True
                break

        if isLogin:
            print("Login successfull")
            break
        else:
            print(f"Either userName or password is incorrect. Maximum attempts remaining {3-attempts}")
            attempts+=1


def registerUser():
    global users
    userN = input("Enter your userName: ")
    passN = input("Enter your password: ")

    users.append({
        "userName": userN,
        "password": passN
    })

    print("Registration successfull.. Redirecting to login")
    loginUser()

def resetPassword():
    global users

    userN = input("Enter your userName: ")
    passN = input("Enter your new password: ")

    isReset = False
    for user in users:
        if user["userName"] == userN:
            user["password"] = passN
            isReset = True
            break

    if isReset:
        print("Password Reset successfull...Redirecting to login")
        loginUser()
    else:
        print("UserName not present please register..redirecting to registration")
        registerUser()


operation = int(input("Enter operation to perform 1. Login 2. Registration 3. Reset Password"))
if operation == 1:
    loginUser()
elif operation == 2:
    registerUser()
elif operation ==3:
    resetPassword()
else:
    print("Invalid operation. try again")
