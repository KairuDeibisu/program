from flask import Flask

app = Flask(__name__)

@app.route("/about")
def about():
    return "<p>About Me!</p>"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(port=80)