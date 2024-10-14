from flask import Flask
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler
import os

app = Flask(__name__)


# Initialize Azure Application Insights telemetry with your Connection String
exporter = AzureExporter(connection_string='InstrumentationKey=eb5ed67c-09c1-4217-9d25-c09b90da6343;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/;ApplicationId=bfc6eeee-bc49-4f69-9676-e1e4b044f50d')

# Set up tracer with a sampling rate (1.0 = 100%, 0.1 = 10% etc.)
tracer = Tracer(exporter=exporter, sampler=ProbabilitySampler(1.0))

@app.route("/")
def hello():
    return "Welcome to Hello-world Python Flask Application"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
