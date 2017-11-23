from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index(name="Yemi"):
    name = request.args.get("name", name)
    return "Hi there {}".format(name)

app.run(debug=True)
