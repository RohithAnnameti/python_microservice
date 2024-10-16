from flask import Flask
import os
import azure.applicationinsights

app_insights_client = azure.applicationinsights.TelemetryClient(
    instrumentation_key='bba9d30b-eb36-4ab9-a814-434c2e7d86b9'
)
app_insights_client.track_event('my_event', {'my_property': 'my_value'})
app_insights_client.track_metric('my_metric', 100)
app_insights_client.track_exception(Exception('my_exception'))
app = Flask(__name__)

azure.applicationinsights.configure(
    app_insights_client,
    collection_interval=1.0,
    collection_type='new'
)
@app.route("/")
def hello():
    return "Welcome to Hello-world Python Flask Application"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
