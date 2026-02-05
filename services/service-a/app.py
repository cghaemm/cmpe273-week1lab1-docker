import time
from flask import Flask, request, jsonify, g
import logging

SERVICE = "service-a"
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
app = Flask(__name__)

@app.before_request
def start_timer():
    g.start = time.time()

@app.after_request
def log_request(resp):
    latency_ms = round((time.time() - g.start) * 1000, 3)
    log_message = f"service-name={SERVICE} endpoint='{request.method} {request.path}' status={resp.status_code} latency_ms={latency_ms}ms"
    logging.info(log_message)
    return resp


@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/echo")
def echo():
    msg = request.args.get("msg", "")
    resp = {"echo": msg}
    return jsonify(resp)


if __name__ == "__main__":
    print("RUNNING SERVICE A")
    app.run(host="0.0.0.0", port=8080)