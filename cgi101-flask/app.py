from flask import Flask, request, jsonify, render_template
import poker as p
import model

app = Flask(
    __name__,
    static_url_path="/source",   # default /static
    static_folder="./tmpfolder"  # default ./static
)


@app.route("/")
def hello():
    print("123123")
    return "<h1>Hello Flask!</h1>"


# @app.route("/hello/<username>")
# def hello_user(username):
#     output = "<h2>Hello {} !!!!!!!!!!!!</h2>"
#     return output.format(username)


@app.route("/hello/<username>")
def hello_user(username):
    return render_template(
        "hello.html",
        username=username
    )


@app.route("/addTwoNum/<x>/<y>")
def addTwoNum(x, y):
    return str(int(x) + int(y))


# /hello_get?name=Allen&age=22
# @app.route("/hello_get")
# def hello_get():
#     name = request.args.get("name")
#     age = request.args.get("age")
#     if name == None:
#         return "What's your name?"
#     elif age == None:
#         return "Hello {} !".format(name)
#     else:
#         output = "Hello {}, you are {} years old."
#         return output.format(name, age)

@app.route("/hello_get")
def hello_get():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template(
        "hello_get.html",
        name=name,
        age=age
    )


@app.route("/hello_post", methods=["GET", "POST"])
def hello_post():
    output = """
    <form action="/hello_post" method="POST">
        <label>What is your name?</label>
        <br>
        <input name="username">
        <button type="submit">Submit</button>
    </form>
    <img src="/source/google.png">
    """
    method = request.method  # -> GET or POST string
    if method == "POST":
        username = request.form.get("username")
        output += """
        <h1>Hello {} !</h1>
        """.format(username)
        return output
    return output

# /poker?player=5
# @app.route("/poker")
# def poker():
#     player = int(request.args.get("player"))
#     outputJson = p.poker(player)
#     return jsonify(outputJson)


@app.route('/poker', methods=['GET', 'POST'])
def poker():
    request_method = request.method
    players = 0
    cards = dict()
    if request_method == 'POST':
        players = int(request.form.get('players'))
        cards = p.poker(players)
    return render_template('poker.html', request_method=request_method,
                                         cards=cards)


@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)


@app.route('/show_staff/salaryGreaterThan/<s>')
def hello_google_2(s):
    staff_data = model.getStaff_salary(s)
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
