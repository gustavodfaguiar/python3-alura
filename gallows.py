def game():
    print("****************************")
    print("Welcome to the gallows game")
    print("****************************")

    secret_word = "banana"
    letters_hit = ["_","_","_","_","_","_"]

    hanged = False
    hit = False

    while not hanged and not hit:
        kick = input("What is the letter? ")
        kick = kick.strip()
        index = 0

        for letter in secret_word:
            if letter.upper() == kick.upper():
                letters_hit[index] = letter
            index = index + 1

        print(letters_hit)


    print("End of the game")

if __name__ == "__main__":
    game()
