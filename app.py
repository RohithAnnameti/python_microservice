# microservice.py
from flask import Flask, jsonify, request
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
# Create Flask app
app = Flask(__name__)
# Replace with your actual Instrumentation Key from Azure Application Insights
INSTRUMENTATION_KEY = 'eb5ed67c-09c1-4217-9d25-c09b90da6343'
# Middleware to automatically trace requests and send telemetry to Azure
middleware = FlaskMiddleware(
   app,
   exporter=AzureExporter(connection_string=f'InstrumentationKey={INSTRUMENTATION_KEY}'),
   sampler=ProbabilitySampler(1.0)  # 1.0 = 100% sampling, 0.1 = 10%, etc.
)
# Configure logging for custom telemetry (optional)
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string=f'InstrumentationKey={INSTRUMENTATION_KEY}'))
@app.route('/greet', methods=['GET'])
def greet_user():
   name = request.args.get('name', 'World')
   logger.info(f"Greeted {name}")  # Log user interaction for telemetry
   return jsonify(message=f"Hello, {name}!")
@app.route('/data', methods=['POST'])
def post_data():
   data = request.json
   logger.info(f"Received data: {data}")  # Log the posted data for telemetry
   return jsonify(received=data)
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
