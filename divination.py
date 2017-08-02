print("****************************")
print("Welcome to the guessing game")
print("****************************")

secret_number = 42
total_of_attempts = 3
rounds = 1

for rounds in range(1, total_of_attempts + 1):

    print("Attempts {} of {}".format(rounds, total_of_attempts))

    kick = input("Enter a number between 1 and 100: ")
    kick = int(kick)

    if kick < 1 or kick > 100:
        print("You must enter a number between 1 and 100")
        continue

    hit = secret_number == kick
    larger = kick > secret_number

    if hit:
        print("You're right")
        break
    else:
        if larger:
            print("You missed! His kick was bigger than the secret number")
        else:
            print("You missed! His kick was less than the secret number")


print("End of the game")
