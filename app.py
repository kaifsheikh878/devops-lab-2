
from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define what happens when someone visits the main page ('/')
@app.route('/')
def hello():
    return "Hello from the DevOps Lab!"

# Run the app on port 8080 when executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)