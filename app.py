from flask import Flask
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler
import os

app = Flask(__name__)

# Configure Application Insights
instrumentation_key = 'eb5ed67c-09c1-4217-9d25-c09b90da6343'  # Replace with your actual Instrumentation Key

# Enable automatic distributed tracing
middleware = FlaskMiddleware(
   app,
   exporter=AzureExporter(connection_string=f'InstrumentationKey={instrumentation_key}'),
   sampler=ProbabilitySampler(1.0)
)

@app.route("/")
def hello():
    return "Welcome to Hello-world Python Flask Application"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
