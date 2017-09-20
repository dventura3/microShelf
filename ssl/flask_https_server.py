from flask import Flask, jsonify
from flask import request


# To create a new certificate & provate key
# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

import ssl
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ctx.load_cert_chain('cert.pem', 'key.pem')




app = Flask(__name__)


@app.route('/')
def index():
	return 'Flask is running!'


@app.route('/data')
def names():
	data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
	return jsonify(data)


@app.route('/api/lockers', methods=['PUT'])
def lockers():
	if request.method == 'PUT':
		data = {"names": ["AAA", "BBB", "CCC", "DDD"]}
		return jsonify(data)
	return 'ERROR'


if __name__ == '__main__':  
	 app.run(host='127.0.0.1', port=5301, debug=True, ssl_context=ctx)