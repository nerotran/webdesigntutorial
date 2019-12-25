from flask import Flask, render_template, url_for
app = Flask(__name__)

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


#if run directly using python, launch in debug mode
if __name__ == '__main__':
    app.run(debug=True)