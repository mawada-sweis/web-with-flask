from crypt import methods
from flask import Flask, render_template, request, redirect, url_for

admins = {
    "admin001":"123",
    "admin002":"456"
}


# create an object of the flask class
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('uname')
    password = request.form.get('psw')
    if name in admins:
        if password == admins[name]:
            return render_template('home_admin.html')
        else: 
            return "Password incorrect"
    else: 
        return "Not Found"

@app.route('/signup/<email>', methods=['POST'])
def search_account(account):
    body = request.body


def create_app():
    """Function to return Flask object
    Returns:
        [app]: [Flask object created]
    """
    return app
