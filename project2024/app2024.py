from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

app = Flask(__name__, template_folder = "templates")
app.config['SECRET_KEY']="123456"
Config = {
  'apiKey': "AIzaSyCm2m7R8XN6Ne6GzdqoBbbPRqOoVBVrB7s",
  'authDomain': "project2024-31a57.firebaseapp.com",
  'projectId': "project2024-31a57",
  'storageBucket': "project2024-31a57.appspot.com",
  'messagingSenderId': "569820173976",
  'appId': "1:569820173976:web:95581d84e6727220d622ed",
  'databaseURL':"https://project2024-31a57-default-rtdb.europe-west1.firebasedatabase.app/"
  }


firebase = pyrebase.initialize_app(Config) 
auth = firebase.auth()
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def signin2024():
    if request.method == 'GET':
        return render_template('signin2024.html')
    else:
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home2024pick'))
        except Exception as e:
            print(e)
            error = "try again"
            return render_template("signin2024.html") 

@app.route('/signup2024', methods=["GET", "POST"])
def signup2024():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user= auth.create_user_with_email_and_password(email, password)
            login_session['user'] = user
            print(login_session['user'])
            print (user)
            return redirect(url_for('home2024pick'))
        except:
            error = "Womp it failed. Try again"
            return render_template("signup2024.html",error=error)
    if request.method == "GET":
        return render_template('signup2024.html')
 
@app.route('/home2024pick', methods=["GET", "POST"])
def home2024pick():
    if request.method == "GET":
        artists = db.get().val()
        print(artists)
        return render_template("home2024pick.html", artists=artists)
    else:
        login_session['user'] = None
        auth.current_user = None
        return redirect(url_for('signin2024.html'))

@app.route("/monte" , methods = ['GET', 'POST']) 
def monte():
    return render_template("monte.html")

@app.route("/<string:name>" , methods = ['GET', 'POST']) 
def artist(name):
    for i in db.get().val().values():
        if i["dbname"] == name:
             return render_template("artist.html", name=name, description=i["dbD"], url=i["dbimage"]) 


    return render_template("monte.html") 

@app.route("/add" , methods = ['GET', 'POST']) 
def add():
    if request.method == "POST":
        name_ofyour_artist = request.form['name_ofyour_artist']
        description = request.form['description']
        insert_image = request.form['insert_image']
        db.push({"dbname": name_ofyour_artist, "dbD": description, "dbimage": insert_image})
        return redirect(url_for('home2024pick'))
    else:
        return render_template("add.html") 


if __name__ == "__main__":
    app.run(debug = True) 
    