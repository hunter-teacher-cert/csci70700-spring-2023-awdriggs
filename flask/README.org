# Cellular Automata Flask App

I was reading about Wolfram Cellular Automata this last week. Never having really gone deep with coding them out, I thought this might be a fun solution to do with flask.

## Routes

### Home 
```python
@app.route("/")
def home():
    return render_template("home.html")
```
Index route displays the home template. I used the jinja for loop to create a link for every automaton. 

![Screenshot of Home](./home.png) 
 
### Cellular Automaton
```python
@app.route('/ca/<int:number>')
def ca(number):
    board = build(number, False) #builds the ca space as a list of rows, each row is a string
    return render_template("test.html", num = number, board = board)
```
This is a dynamic route that creates an endpoint for any particular automaton that is requested, i.e. `localhost:5000/ca/110` will take you to the page for automaton 110. 
The automaton is built by a helper function then sent as a list to the template. The template then loops through the list and builds the automaton using `div` tags. 

![Screenshot of CA 110](./110.png)
 
### Random Automaton  
```python
@app.route('/ca/<int:number>/random')
def random_seed(number):
    board = build(number, True) #builds the ca space as a list of rows, each row is a string
    return render_template("test.html", num = number, board = board)
```
This is another dynamic route that uses the same template as the other CA route. In this instance, the helper function builds the automaton with a random seed row instead of the standard cell black cell in the middle of the CA space.  

![Screenshot of CA 110](./110r.png)
