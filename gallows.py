import random

def print_opening_message():
    print("****************************")
    print("Welcome to the gallows game")
    print("****************************")

def carry_the_secret_word():
    file_gallow = open("words.txt", "r")
    words = []

    for line in file_gallow:
        line = line.strip()
        words.append(line)

    file_gallow.close()

    number = random.randrange(0, len(words))
    return words[number].upper()

def initialize_successfull_lyrics(secret_word):
    return [ "_" for letter in secret_word ]

def call_for_the_kick():
    kick = input("What is the letter? ")
    kick = kick.strip().upper()
    return kick

def correct_kick_mark(kick, letters_hit, secret_word):
    index = 0
    for letter in secret_word:
        if letter == kick:
            letters_hit[index] = letter
        index += 1

def print_success_message():
    print("You won!!")

def print_lost_message():
    print("Yout lost!!")

def game():
    print_opening_message()
    secret_word = carry_the_secret_word()
    letters_hit = initialize_successfull_lyrics(secret_word)
    print(letters_hit)

    hanged = False
    hit = False
    errors = 0

    while not hanged and not hit:
        kick = call_for_the_kick()

        if kick in secret_word:
            correct_kick_mark(kick, letters_hit, secret_word)
        else:
            errors += 1

        hanged = errors == 6
        hit = "_" not in letters_hit
        print(letters_hit)


    if hit:
        print_success_message()
    else:
        print_lost_message()

    print("End of the game")

if __name__ == "__main__":
    game()
