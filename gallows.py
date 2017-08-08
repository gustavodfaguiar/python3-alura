def game():
    print("****************************")
    print("Welcome to the gallows game")
    print("****************************")

    secret_word = "banana"
    hanged = False
    hit = False

    while not hanged and not hit:
        kick = input("What is the letter? ")
        kick = kick.strip()
        index = 0

        for letter in secret_word:
            if letter.upper() == kick.upper():
                print("I found the letter {} in the {}".format(letter, index))
            index = index + 1

        print("playing...")


    print("End of the game")

if __name__ == "__main__":
    game()
