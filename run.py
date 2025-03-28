from flask import Flask

app = Flask(__name__)

@app.route('/')
def mainpage():
    return "<h1>Welcome to micro-planner!</h1>"


if __name__ == "__main__":
    app.run(debug=True)