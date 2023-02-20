# save this as app.py
from flask import Flask, render_template, session, url_for, redirect, request
from helpers import build #here be the cellular automata function

app = Flask(__name__)
app.secret_key = "281c16d162021c6b43a01ca2f388dfc6761bf45ff494cb67eef217ab0f16c635" 

@app.route("/")
def home():
    return render_template("home.html", sesh=session)

@app.route("/about")
def about():
    return "about"

@app.get('/ca/<int:number>/random')
def random_seed(number):
    board = build(number, True) #builds the ca space as a list of rows, each row is a string 
    return render_template("automata.html", num = number, board = board, sesh=session)

@app.get('/ca/<int:number>')
def ca(number):
    board = build(number, False) #builds the ca space as a list of rows, each row is a string 
    return render_template("automata.html", num = number, board = board, sesh=session)
 
@app.post('/ca/<int:number>')
def ca_post(number):
    # print(request.form['submit'])
    if "likes" not in session:  #add a likes key to session if there isn't one
        session["likes"] = {}

    l = session["likes"] #temp copy of likes

    if request.form['submit'] == "Unlike": #if a ca is unliked, pop it from the list
        l.pop(str(number)) 
    else:
        l[str(number)] = True #meaning it has been liked, so add a key with value == true
    
    session["likes"] = l #set session to the updated copy of likes
    # return render_template("test.html", session=session)
    return redirect(url_for('.ca', number = number))

#just for spying session data 
@app.route("/session")
def sesh():
    return render_template("test.html", session=session)
