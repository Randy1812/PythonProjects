from flask import Flask
import random

rnum = random.randint(0, 9)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a Number between 0 and 9</h1><br><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:num>')
def rndnum(num):
    if num > rnum:
        return f"<h1 style='color:purple'>Too High Try Again!</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif num < rnum:
        return f"<h1 style='color:red'>Too Low Try Again!</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return f"<h1 style='color:green'>You Found Me!</h1><br><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
