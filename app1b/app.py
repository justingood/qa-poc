import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    r = requests.get('http://app2.default') # app2a in the 'default' namespace
    hello = 'Hello from app1b and ' + r.text
    return hello

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
