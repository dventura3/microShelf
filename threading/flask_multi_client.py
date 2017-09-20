from flask import Flask, jsonify
from flask import request
import requests
import json


app = Flask(__name__)

# curl -H "Content-Type: application/json" -X PUT http://127.0.0.1:5300/

@app.route('/', methods=['PUT'])
def index():
	url = "http://127.0.0.1:5301/api/lockers";
	try:
		print('>> Before making the /api/lockers request')
		
		payload = {'lockerID': 'A1', 'mode': 'default'}
		headers = {"content-type": "application/json"}
		r = requests.put(url, data=json.dumps(payload), headers=headers)

		print(r.status_code)
		print(r.json())
		print('>> Request /api/lockers completed!')
		return 'OK'
	except requests.exceptions.RequestException as e:
		print(e)
		return 'ERROR'


@app.route('/data')
def data_func():
	url = "http://127.0.0.1:5301/data";
	try:
		print('>> Before making the /data request')
		r = requests.get(url)
		print(r.status_code)
		print(r.json())
		print('>> Request /data completed!')
		return 'OK'
	except requests.exceptions.RequestException as e:
		print(e)
		return 'ERROR'


if __name__ == '__main__':  
	 app.run(host='127.0.0.1', port=5300, debug=True, threaded=True)