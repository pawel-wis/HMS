from flask import Flask, render_template

app = Flask(__name__)

APP_TITLE = "HMS"


@app.route("/")
def index():
    return render_template('index.html', title=APP_TITLE)


if __name__ == '__main__':
    app.run()
