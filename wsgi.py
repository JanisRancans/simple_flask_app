from flask import Flask
from flask import request
application = Flask(__name__)

@application.route('/')
def hello_ip():
    return request.headers.get('X-Forwarded-For', request.remote_addr)

if __name__ == "__main__":
    application.run()
