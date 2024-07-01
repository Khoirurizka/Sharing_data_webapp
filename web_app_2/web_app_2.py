from flask import Flask, request, render_template_string

app = Flask(__name__)

data_received = {}

@app.route('/')
def index():
    global data_received
    return render_template_string('''
        <h1>Data Received</h1>
        <p>Robot Type: {{ data_received.get('robot_type', '') }}</p>
        <p>Robot ID: {{ data_received.get('robot_id', '') }}</p>
        <p>Command: {{ data_received.get('command', '') }}</p>
        <p>Argument 1: {{ data_received.get('argument_1', '') }}</p>
        <p>Argument 2: {{ data_received.get('argument_2', '') }}</p>
        <p>Argument 3: {{ data_received.get('argument_3', '') }}</p>
    ''', data_received=data_received)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    global data_received
    data_received = request.get_json()
    for key, value in data_received.items():
        print(f'{key}: {value}')
    return 'Data received successfully!', 200

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5001)

