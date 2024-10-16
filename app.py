from flask import Flask
import os
import logging
from azure.applicationinsights import TelemetryClient
# Initialize the TelemetryClient with the Instrumentation Key
telemetry_client = TelemetryClient.from_connection_string(
    "InstrumentationKey=bba9d30b-eb36-4ab9-a814-434c2e7d86b9"
)

def track_event(event_name, properties=None):
    telemetry_client.track_event(event_name, properties)

def track_metric(metric_name, value):
    telemetry_client.track_metric(metric_name, value)

def track_exception(exception):
    telemetry_client.track_exception(exception)
    
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Hello-world Python Flask Application"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
