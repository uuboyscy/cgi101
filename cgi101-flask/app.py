from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    print("123123")
    return "<h1>Hello Flask!</h1>"


@app.route("/hello/<username>")
def hello_user(username):
    output = "<h2>Hello {} !!!!!!!!!!!!</h2>"
    return output.format(username)


@app.route("/addTwoNum/<x>/<y>")
def addTwoNum(x, y):
    return str(int(x) + int(y))


# /hello_get?name=Allen&age=22
@app.route("/hello_get")



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
