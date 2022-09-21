import copy
from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session
from tempfile import mkdtemp

from minimax import TicTacToe
from minimax import minimax_decision
from constants import BLANK

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():

    if "board" not in session:
        session["board"] = [[BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK]]
        session["turn"] = "o"

    return render_template("board.html", game=session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    game = TicTacToe()
    grid = copy.deepcopy(session["board"])
    while (not game.terminal_test(grid)):
    
        if session["turn"] == "o":
            comp = minimax_decision(game,session["board"])
            r, c= comp[0], comp[1]
            session["board"][r][c] = 'o'
            session["turn"] = "x"
        elif session["turn"] == "x":
            if session["board"][row][col] == BLANK:
                session["board"][row][col] = 'x'
                session["turn"] = "o"

    return redirect(url_for("index"))


@app.route('/reset', methods=["GET", "POST"])
def button():
    if request.method == "POST":
        session["board"] = [[BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK], [BLANK, BLANK, BLANK]]
        session["turn"] = "o"
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)