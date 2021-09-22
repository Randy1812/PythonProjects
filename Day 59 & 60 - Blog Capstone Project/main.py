from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
emailid1 = os.getenv("USERID1")
emailid2 = os.getenv("USERID2")
pswd = os.getenv("PSWD")

app = Flask(__name__)

data = requests.get('https://api.npoint.io/7ebefb244ec34cfe8eb3')
all_posts = data.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


def send_email(name, email, phone, msg):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(emailid1, pswd)
        connection.sendmail(emailid1, emailid2, email_message)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template('contact.html', h1cont="Contact Me")
    elif request.method == "POST":
        data = request.form
        send_email(data['name'], data['email'], data['phone'], data['message'])
        return render_template('contact.html', h1cont="Successfully sent your message.")


@app.route("/post/<int:postid>")
def post(postid):
    return render_template("post.html", post=all_posts[postid - 1])


if __name__ == "__main__":
    app.run(debug=True)
