from flask import Flask
import math

app = Flask(__name__)

@app.route('/')
def home():
    result = 0
    for i in range(1, 10_000_000):
        result += math.sqrt(i)
    return f"Green service version 2.0 — result: {result:.2f}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)