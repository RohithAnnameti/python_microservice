from flask import Flask
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler
import os

app = Flask(__name__)


# Import the `configure_azure_monitor()` function from the
# `azure.monitor.opentelemetry` package.
from azure.monitor.opentelemetry import configure_azure_monitor

# Import the tracing api from the `opentelemetry` package.
from opentelemetry import trace

# Configure OpenTelemetry to use Azure Monitor with the 
# APPLICATIONINSIGHTS_CONNECTION_STRING environment variable.    
# Import the `configure_azure_monitor()` function from the `azure.monitor.opentelemetry` package.
from azure.monitor.opentelemetry import configure_azure_monitor

# Configure OpenTelemetry to use Azure Monitor with the specified connection string.
# Replace `<your-connection-string>` with the connection string of your Azure Monitor Application Insights resource.
configure_azure_monitor(
    connection_string="InstrumentationKey=eb5ed67c-09c1-4217-9d25-c09b90da6343;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/;ApplicationId=bfc6eeee-bc49-4f69-9676-e1e4b044f50d",
)
...
configure_azure_monitor(
	enable_live_metrics=True
)
...

@app.route("/")
def hello():
    return "Welcome to Hello-world Python Flask Application"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
