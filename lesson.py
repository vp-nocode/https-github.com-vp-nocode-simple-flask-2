from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def films():
    context = {
        "caption": "Movies",
        "list": ["Nina", "Karina", "Anton", "Nikita"],
        "link": "/"
    }
    return render_template("movies.html", **context)

@app.route("/person/")
def person():
    context = {
        "caption": "Heroes of movies",
        "link": "/person/"
    }
    return render_template("heroes.html",  **context)


if __name__ == "__main__":
    app.run()