from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", result=None, x=None)


@app.route("/predict", methods=["POST"])
def predict():
    x = int(request.form["x"])
    result = x * 2
    return render_template("index.html", result=result, x=x)


if __name__ == "__main__":
    app.run(debug=True)
