import gallows
import divination

print("****************************")
print("Choose your game")
print("****************************")

print("(1) Gallows (2) Divination")

game = int(input("What game? "))

if game == 1:
    print("Game gallows")
    gallows.game()
elif game == 2:
    print("Game divination")
    divination.game()

print("End of the game")

