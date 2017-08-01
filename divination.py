print("****************************")
print("Welcome to the guessing game")
print("****************************")

secret_number = 42
kick = input("Enter your number: ")
kick = int(kick)

hit = secret_number == kick
larger = kick > secret_number

if hit:
    print("You're right")
else:
    if larger:
        print("You missed! His kick was bigger than the secret number")
    else:
        print("You missed! His kick was less than the secret number")

print("End of the game")
