from flask import Flask
from flask import request
application = Flask(__name__)

@application.route('/')
def hello_ip():
    message = "Hello, {}".format(request.headers.get('X-Forwarded-For', request.remote_addr))
    return message

if __name__ == "__main__":
    application.run()
