# save this as app.py
from flask import Flask
from flask import render_template
from helpers import build #here be the cellular automata function

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return "about"

@app.route('/ca/<int:number>/random')
def random_seed(number):
    board = build(number, True) #builds the ca space as a list of rows, each row is a string 
    return render_template("test.html", num = number, board = board)

@app.route('/ca/<int:number>')
def ca(number):
    board = build(number, False) #builds the ca space as a list of rows, each row is a string 
    return render_template("test.html", num = number, board = board)

# @app.context_processor
# def inject_rules():
#     rules = ["111", "110", "101", "100", "011", "010", "001", "000"] #the rules
#     return dict(user="adam", rules=rules)

# @app.context_processor
# def utility_processor():
#     def format_price(amount, currency="€"):
#         return f"{amount:.2f}{currency}"
#     def get_set(num):
#         return list("{:08b}".format(num)) #list of the binary representation of the rule set number as a sring
#     return dict(format_price=format_price, get_set=get_set)

# # functions for the templates
# def clever_function():
#     return u'HELLO'

# app.jinja_env.globals.update(clever_function=clever_function, stupid=stupid, get_seed=get_seed, automate=automate)
 
