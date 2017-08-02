print("****************************")
print("Welcome to the guessing game")
print("****************************")

secret_number = 42
total_of_attempts = 3
rounds = 1

while rounds <= total_of_attempts:

    print("Attempts {} of {}".format(rounds, total_of_attempts))

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

    rounds = rounds + 1

print("End of the game")
