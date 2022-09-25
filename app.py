# importing libraries
import copy
from datetime import timedelta
from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session
from tempfile import mkdtemp

# import modules
from game import TicTacToe
from minimaxalgo import minimax_decision
from constants import BLANK

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=5)
Session(app)

@app.route("/")
def index():

    if "board" not in session:
        session["board"] = [[BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK]]
        session["player"] = "x"
        session["GameResults"] = None

    return render_template("board.html", game=session["board"], player=session["player"], winner = session["GameResults"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    game = TicTacToe()
    # if "board" in session:
    #     grid = copy.deepcopy(session["board"])
    if not game.terminal_test(session["board"]):
    
        if session["player"] == "o":
            comp = minimax_decision(game,session["board"])
            r, c= comp[0], comp[1]
            session["board"][r][c] = 'o'
            session["player"] = "x"
        elif session["player"] == "x":
            if session["board"][row][col] == BLANK:
                session["board"][row][col] = 'x'
                session["player"] = "o"

    # Checking if the game is over and if it is, it prints the winner.
    else:
        winner = game.winner(session["board"])
        if (winner != BLANK):
            session["GameResults"] = winner
        else:
            session["GameResults"] = "It was a draw."

    return redirect(url_for("index"))


@app.route('/reset', methods=["GET", "POST"])
def button():
    if request.method == "POST":
        session["board"] = [[BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK]]
        session["player"] = "x"
        session["GameResults"] = None
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)