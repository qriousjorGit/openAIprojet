from flask import Flask, render_template, request, redirect, url_for, flash
from main import get_sentences
import smtplib
from send_mail import send_email

OWN_EMAIL = "ielts.trainer.2010@gmail.com"
OWN_PASSWORD = "uedjbbmhtbmbdfyn"

app = Flask(__name__)
app.secret_key = "generic key"

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/sentences", methods=["POST"])
def get_data():
    target = request.form["target"]
    sentences = get_sentences(target)
    return f"<h3>Here are your examples: </h3> <p>{sentences}</p>"

@app.route("/vocabengine", methods=["POST", "GET"])
def sentences_page():
    if request.method == 'GET':
        return render_template('sentences.html')



@app.route("/email", methods=["POST"])
def send_message():
    data = request.form
    # print(type(data))
    # print(data['name'])
    # print(data['email'])
    name = data['name']
    email = data['email']
    message = data['messagRoe']
    #TODO flash doesn't work
    # flash('You were successfully logged in')
    send_email(name=name, email=email, phone='none', message=message)
    return f"<h3>Message sent!</h3> <p>{data['name']} <br> {data['email']} <br> {data['messagRoe']}</p>"




if __name__ == "__main__":
    app.run(debug=True)