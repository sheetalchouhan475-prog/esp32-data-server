from flask import Flask, request

app = Flask(_name_)

@app.route('/')
def home():
    return "Server Running"

@app.route('/data')
def data():
    value = request.args.get('value')
    print("Sensor Data:", value)
    return "Data Received"

app.run(host='0.0.0.0', port=10000)
