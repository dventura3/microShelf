from flask import Flask, jsonify
import requests

# openssl req -x509 -newkey rsa:4096 -nodes -out cert_2.pem -keyout key_2.pem -days 365

# If you get the error:
'''
The problem is not in your code but in the web site you are trying to access. When looking at the analysis by SSLLabs you will note.
This server's certificate chain is incomplete. Grade capped to B.
This means that the server configuration is wrong and that not only python but several others will have problems with this site. Some desktop browsers work around this configuration problem by trying to load the missing certificates from the internet or fill in with cached certificates. But other browsers or applications will fail too, similar to python.

To work around the broken server configuration you might explicitly extract the missing certificates and add them to you trust store. Or you might give the certificate as trust inside the verify argument.
You can pass verify the path to a CA_BUNDLE file or directory with certificates of trusted CAs:
>>> requests.get('https://github.com', verify='/path/to/certfile') 
This list of trusted CAs can also be specified through the REQUESTS_CA_BUNDLE environment variable.

In alternative:
r = requests.put(url, verify=False)
'''

import ssl
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ctx.load_cert_chain('cert_2.pem', 'key_2.pem')




app = Flask(__name__)


@app.route('/')
def index():
	url = "https://127.0.0.1:5301/api/lockers";
	try:
		print('Before making the https request')
		r = requests.put(url)
		print(r.status_code)
		print('Request done!')
		return 'OK'
	except requests.exceptions.RequestException as e:  # This is the correct syntax
		print(e)
		return 'ERROR'


if __name__ == '__main__':  
	 app.run(host='127.0.0.1', port=5300, debug=True, ssl_context=ctx)