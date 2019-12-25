from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "a6bb7f1051ee12ddf5a203331b51758b"

posts = [
    {
        "title": "First post",
        "author": "Nero",
        "date": "Aug 10",
        "content": "content"
    },
    {
        "title": "Second post",
        "author": "Nero",
        "date": "Oct 10",
        "content": "content 2"
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

#if run directly using python, launch in debug mode
if __name__ == '__main__':
    app.run(debug=True)