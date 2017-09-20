from flask import Flask, jsonify
from flask import request
import time


app = Flask(__name__)


@app.route('/')
def index():
	return 'Flask is running!'


@app.route('/data')
def names():
	time.sleep(5)
	data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
	return jsonify(data)


# curl -H "Content-Type: application/json" -X PUT -d '{ "lockerID": "A2" }' http://127.0.0.1:5301/api/lockers

@app.route('/api/lockers', methods=['PUT'])
def lockers():
	if request.method == 'PUT':
		try:
			# "d" can be empty! ( d = {} is fine!)
			# But if there is not a JSON, we will get the exception.
			d = request.get_json()
			print('Message received: %s' % d)
		except:
			resp = jsonify({'msg': 'Error: malformed json data'})
			resp.status_code = 400
			return resp

		time.sleep(20)
		data = {"names": ["AAA", "BBB", "CCC", "DDD"]}
		return jsonify(data)
	return 'ERROR'


if __name__ == '__main__':  
	 app.run(host='127.0.0.1', port=5301, debug=True)