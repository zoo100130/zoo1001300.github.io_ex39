from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

PERSON = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

APP_INFO = {
    "id": 5,
    "name": "Python - Flask",
    "version": "1.0.1",
    "author": "Enoxs",
    "remark": "Python - Web Framework",
}

FRUITS = {
    "apple": {
        "title": "Apple",
        "color": "Red",
        "description": "A crisp fruit page loaded from apple.html.",
    },
    "banana": {
        "title": "Banana",
        "color": "Yellow",
        "description": "A bright fruit page loaded from banana.html.",
    },
    "orange": {
        "title": "Orange",
        "color": "Orange",
        "description": "A fresh fruit page loaded from orange.html.",
    },
}


@app.route("/")
def home():
    exercises = [
        {
            "number": "39 / 44",
            "title": "Hello Flask",
            "url": "/hello",
            "summary": "Create a local Flask server and show that it is running.",
        },
        {
            "number": "40 / 45",
            "title": "URL Info",
            "url": "/user/John",
            "summary": "Show information passed through the URL.",
        },
        {
            "number": "41 / 46",
            "title": "Load HTML",
            "url": "/apple",
            "summary": "Load different HTML pages for different URLs.",
        },
        {
            "number": "42 / 47",
            "title": "Show Variables",
            "url": "/variables",
            "summary": "Display a Python object inside a Flask template.",
        },
        {
            "number": "48",
            "title": "Double Number",
            "url": "/double",
            "summary": "Input a number and display double the value.",
        },
    ]
    return render_template("home.html", exercises=exercises)


@app.route("/hello")
def hello():
    return render_template(
        "hello.html",
        title="Hello Flask",
        message="Hello, World!",
        status="The Flask server is running.",
    )


@app.route("/user/<username>")
def show_user_profile(username):
    return render_template(
        "url_info.html",
        title="User Profile",
        label="username",
        value=escape(username),
        route="/user/<username>",
    )


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return render_template(
        "url_info.html",
        title="Post",
        label="post_id",
        value=post_id,
        route="/post/<int:post_id>",
    )


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return render_template(
        "url_info.html",
        title="Path",
        label="subpath",
        value=escape(subpath),
        route="/path/<path:subpath>",
    )


@app.route("/apple")
def apple():
    return render_template("apple.html", fruit=FRUITS["apple"])


@app.route("/banana")
def banana():
    return render_template("banana.html", fruit=FRUITS["banana"])


@app.route("/orange")
def orange():
    return render_template("orange.html", fruit=FRUITS["orange"])


@app.route("/page/app")
def page_app_info():
    return render_template("page.html", appInfo=APP_INFO, text="Python Flask !")


@app.route("/variables")
def variables():
    return render_template("variables.html", person=PERSON)


@app.route("/double")
def double_form():
    return render_template("index.html", result=None, x=None)


@app.route("/predict", methods=["POST"])
def predict():
    x = int(request.form["x"])
    result = x * 2
    return render_template("index.html", result=result, x=x)


if __name__ == "__main__":
    app.run(debug=True)
