from flask import Flask
from flask import request

application = Flask(__name__)

@application.route('/ip', methods=['GET'])
def hello_ip():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)
