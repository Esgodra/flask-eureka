from flask import Flask, request
import pandas as pd
import py_eureka_client.eureka_client as eureka_client

rest_port = 8050
eureka_client.init(eureka_server="http://localhost:8080/eureka",
										app_name="data-service",
										instance_port=rest_port )

app = Flask(__name__)

@app.route("/servicio", methods=['POST'])
def service():
	data = request.json
	df = pd.DataFrame(data, index=[0])
	response = df.describe().to_json()
	return response

if __name__ == "__main__":
	app.run(hots='0.0.0.0', port = rest_port)