from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def welcome():
    html = '<html><body><h1>Welcome<h1></body></html>'
    return html

@app.get('/welcome/<status>')
def welcome_home(status):
    html = f"<html><body><h1>Welcome {status}<h1></body></html>"
    return html

# @app.get('/welcome/back')
# def welcome_back():
#     html = '<html><body><h1>Welcome Back<h1></body></html>'
#     return html


