from flask import Flask
import Milestone4

app = Flask(__name__)

@app.route('/')
def home():
    result = Milestone4.get_output()
    return f"<h1>{result}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
