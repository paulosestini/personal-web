from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory("../src", "index.html")


@app.route("/<path:filename>")
def serve_html(filename):
    if len(filename.split(".")) == 1:
        filename += ".html"
    return send_from_directory("../src", filename)


if __name__ == "__main__":
    app.run(debug=True)
