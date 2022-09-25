from play_cli import play_with_comp
from app import app

def start_game(name):
    print("WELCOME " + name + ", TO THIS GAME!" + 2*"\n") 
    flag = True
    while flag:
        platform = input('Enter CLI to play in the terminal or WEB to play on the web: ')
        if platform.upper() == "CLI":
            flag = False
            play_with_comp(name)
        elif platform.upper() == "WEB":
            flag = False
            app.run()

        else:
            print("Invalid platform!! Try again")

    return None

print()
name=input("Please Enter your name to start the game: ")
if name !=" ":
    start_game(name)
    