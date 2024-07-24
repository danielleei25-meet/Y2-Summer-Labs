from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY']="123456"

firebase = pyrebase.initialize_app(Config) 
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("sigin.html") 
    else: 
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "TRY AGAIN"
            return render_template("signin.html", error=error)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        return render_template("signup.html") 
    else: 
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            print(login_session['user'])
            print(login_session['user']['localId'])
            return redirect(url_for('home'))
        except:
            error = "TRY AGAIN"
            return render_template("signup.html",error=error)

@app.route('/signout')
def signout():
	login_session['user'] = None
auth.current_user = None
return redirect(url_for('signin'))

   
