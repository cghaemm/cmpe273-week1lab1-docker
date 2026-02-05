from flask import Flask, request, jsonify, g
import time
import logging
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
app = Flask(__name__)

SERVICE_A = "http://127.0.0.1:8080"
SERVICE = "service-b"
TIMEOUT_SECONDS = 1.0

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
    return jsonify(status="ok")

@app.get("/call-echo")
def call_echo():
    start = time.time()
    msg = request.args.get("msg", "")
    try:
        r = requests.get(f"{SERVICE_A}/echo", params={"msg": msg}, timeout=TIMEOUT_SECONDS)
        r.raise_for_status()
        data = r.json()
        return jsonify(service_b="ok", service_a=data)
    except Exception as e:
        logging.exception(f"service={SERVICE} endpoint=/call-echo | call to service-a failed: {e}")
        return jsonify(service_b="ok", service_a="unavailable", error=str(e)), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
