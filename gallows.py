def game():
    print("****************************")
    print("Welcome to the gallows game")
    print("****************************")

    secret_word = "banana".upper()
    letters_hit = [ "_" for letter in secret_word ]

    hanged = False
    hit = False
    errors = 0

    print(letters_hit)

    while not hanged and not hit:
        kick = input("What is the letter? ")
        kick = kick.strip().upper()

        if kick in secret_word:
            index = 0
            for letter in secret_word:
                if letter == kick:
                    letters_hit[index] = letter
                index += 1
        else:
            errors += 1

        hanged = errors == 6
        hit = "_" not in secret_word
        print(letters_hit)


    if hit:
        print("You won")
    else:
        print("You lost")

    print("End of the game")

if __name__ == "__main__":
    game()
