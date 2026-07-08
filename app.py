from flask import Flask
from sympy import symbols, expand

app = Flask(__name__)

@app.route("/")
def home():
    x = symbols("x")
    return f"SymPy Output: {expand((x+1)**5)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)