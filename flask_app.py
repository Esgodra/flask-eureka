from flask import Flask, request, jsonify
import pandas as pd
import py_eureka_client.eureka_client as eureka_client

rest_port = 8050
eureka_client.init(eureka_server="http://localhost:8080/eureka",
										app_name="data-service",
										instance_port=rest_port )

app = Flask(__name__)

@app.route("/servicio", methods=['GET'])
def service():
	response = {}
	response['data'] = [{"frijol":"25","arroz":"26","harina":"10", "papa":"50"}]
	response['status'] = "Success"
	response['detail'] = ""
	return jsonify(response), 200

if __name__ == "__main__":
	app.run(host='0.0.0.0', port = rest_port)