from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Working"

@app.route("/check")
def check():
    return "shit is working"

if __name__ == "__main__":
    app.run()