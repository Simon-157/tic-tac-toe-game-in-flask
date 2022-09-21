from play_cli import play_with_comp
from app import app

def start_game(name):
    print("WELCOME " + name + ", TO THIS GAME!" + 2*"\n") 
    platform = input('Enter CLI to play in the terminal or WEB to play on the web: ')
    if platform == "CLI":
        play_with_comp()
    elif platform == "WEB":
        app.run(debug=True)

    return None

print()
name=input("Please Enter your name to start the game: ")
start_game(name)