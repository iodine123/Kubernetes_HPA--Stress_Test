from flask import Flask, request
import math
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'service'])

@app.route('/')
def home():
    REQUESTS.labels(method='GET', endpoint='/', service='Blue_service').inc() 
    result = 0
    for i in range(1, 10_000_000): 
        result += math.sqrt(i)
    return f"Blue service version 2.0 — result: {result:.2f}"

# Endpoint Prometheus scrape
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
