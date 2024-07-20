from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/fortune')
def fortune():
    the_fortunes = ["you will have the best year ever",
    "you will pase all of your exams",
    "you will have alot of money",
    "you will eat the best food today", 
    "you will live a life full of happiness",
    "you will open a successful buisenes",
    "you will have a wonderful family",
    "you will live life to the fullest",
    "you will travel the world",
    "you will become a great leader"
]
    a=random.randint(0,3)
    random_var=the_fortunes[a]
    return render_template("fortune.html",random_var=random_var)


if __name__ == '__main__':
    app.run(debug = True)













