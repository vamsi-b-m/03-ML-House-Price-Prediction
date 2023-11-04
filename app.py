from housing.logger import logging
from flask import Flask


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    logging.info("Testing the log files")
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)