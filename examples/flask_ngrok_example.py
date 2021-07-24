from flask import Flask

from flask_ngrok import run_with_ngrok

app = Flask(__name__)


def register_ngrok_address(address):
    print('Registered ngrok address: {}'.format(address))

run_with_ngrok(app, register_ngrok_address, token)  # Start ngrok when app is run

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
