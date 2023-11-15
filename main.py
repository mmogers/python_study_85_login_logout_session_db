from flask import Flask, request, redirect, render_template, session
from replit import db
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.environ['secretKey']

# Check if the database and sessions are initialized
if "users" not in db:
    db["users"] = {}

@app.route('/', methods=["GET", "POST"])
def index():
    if "username" not in session or session["username"] not in db["users"]:
        return render_template('index.html')
    else:
      page = ""
      username = ""
      page+=f"<h1>{session['username']}</h1>"
      f = open("templates/index.html", "r")
      page+=f.read()
      f.close()
      return page

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/loginprocess', methods=["POST"])
def loginprocess():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in db["users"] and db["users"][username]["password"] == password:
        # Set the username in the session
        session["username"] = username
        return redirect('/')
    else:
        return "Not found"

@app.route('/process', methods=["POST"])
def process():
    form = request.form
    username = form.get("username")
    password = form.get("password")
    name = form.get("name")

    # Store user data in the "users" dictionary
    db["users"][username] = {"username": username, "password": password, "name": name}

    # Set the username in the session
    session["username"] = username

    return redirect("/")


@app.route('/logout')
def logout():
    return render_template("logout.html") 
  
@app.route("/reset",methods=["POST"])
def reset():
  session.clear()
  return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
