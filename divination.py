import random

def game():
    print("****************************")
    print("Welcome to the guessing game")
    print("****************************")

    secret_number = random.randrange(1, 101)
    total_of_attempts = 0
    points = 1000

    print("What level of difficulty?")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Set the level: "))

    if level == 1:
        total_of_attempts = 20
    elif level == 2:
        total_of_attempts = 10
    else:
        total_of_attempts = 5

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
            print("You're right and did {} points!".format(points))
            break
        else:
            if larger:
                print("You missed! His kick was bigger than the secret number")
            else:
                print("You missed! His kick was less than the secret number")
            lost_points = abs(secret_number - kick)
            points = points - lost_points

    print("End of the game")

if __name__ == "__main__":
    game()
