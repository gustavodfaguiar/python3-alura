print("****************************")
print("Welcome to the guessing game")
print("****************************")

secret_number = 42
kick = input("Enter your number: ")
kick = int(kick)

if secret_number == kick:
    print("You're right")
else:
    print("You missed")
