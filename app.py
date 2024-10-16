from flask import Flask
import os

@app.route("/")
def hello():
    return "Welcome to Hello-world Python Flask Application"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
