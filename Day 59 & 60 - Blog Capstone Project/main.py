from flask import Flask, render_template
import requests

app = Flask(__name__)

data = requests.get('https://api.npoint.io/7ebefb244ec34cfe8eb3')
all_posts = data.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/post/<int:postid>")
def post(postid):
    return render_template("post.html", post=all_posts[postid - 1])


if __name__ == "__main__":
    app.run(debug=True)
