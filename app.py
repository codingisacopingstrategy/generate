from flask import Flask
app = Flask(__name__)

import kgp

@app.route("/")
def hello():
    e = kgp.KantGenerator('kant.xml')
    return e.output()

if __name__ == "__main__":
    app.run()
