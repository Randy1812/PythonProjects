from flask import Flask, render_template
import requests

app = Flask(__name__)

data = requests.get('https://api.npoint.io/aa0d7f55d87e901a7469')
all_posts = data.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:postid>')
def post(postid):
    return render_template('post.html', post=all_posts[postid - 1])


if __name__ == "__main__":
    app.run(debug=True)
