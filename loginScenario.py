userName = "Vignesh"
password = "Vignesh"

attempts = 1

while attempts <= 4:

    if attempts == 4:
        print("Maximum attempts reached")
        break

    user = input("Enter UserName: ")
    passwordN = input("Enter your password: ")

    if user == userName and password == passwordN:
        print("logged in successfully")
        break
    else:
        print(f"either userName or password is incorrect. attempts remaining {3-attempts}")
        attempts += 1
