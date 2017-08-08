import random

def game():
    print("****************************")
    print("Welcome to the gallows game")
    print("****************************")

    file_gallow = open("words.txt", "r")
    words = []

    for line in file_gallow:
        line = line.strip()
        words.append(line)

    file_gallow.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()

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
        hit = "_" not in letters_hit
        print(letters_hit)


    if hit:
        print("You won")
    else:
        print("You lost")

    print("End of the game")

if __name__ == "__main__":
    game()
