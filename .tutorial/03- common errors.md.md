# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## SSSSHHHHHHHHH

👉 What's the problem here?


```python
from flask import Flask, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "THIS_IS_THE_SECRET_KEY"

@app.route('/')

def index():
  page = ""
  myName = ""
  if session["myName"]:
    myName = session["myName"]
  page += f"<h1>{myName}</h1>"
  f = open("form.html", "r")
  page += f.read()
  f.close()
  return page

@app.route("/setName", methods=["POST"])

def setName():
  session["myName"] = request.form["name"]
  return redirect("/")

@app.route("/reset")
def reset():
  session.clear()
  return redirect("/")

app.run(host='0.0.0.0', port=81)
```

<details> <summary> 👀 Answer </summary>

Yep, you got it!  My secret key was hard coded into my source code. Anyone with access to the code can now use the key to decrypt the contents of the session.  Nice!

```python
app.secret_key = os.environ['sessionKey']
```

</details>

## Informal

👉 What's the problem here?


```python

from flask import Flask, request, redirect, session
import os

app = Flask(__name__)

@app.route('/')

def index():
  page = ""
  myName = ""
  if session["myName"]:
    myName = session["myName"]
  page += f"<h1>{myName}</h1>"
  f = open("form.html", "r")
  page += f.read()
  f.close()
  return page

@app.route("/setName", methods=["POST"])

def setName():
  session["myName"] = request.form["name"]
  return redirect("/")

@app.route("/reset")
def reset():
  session.clear()
  return redirect("/")

app.run(host='0.0.0.0', port=81)
```
<details>
  
In this one, I've forgotten to set a secret key entirely. This will throw an **internal server error**.


</details>