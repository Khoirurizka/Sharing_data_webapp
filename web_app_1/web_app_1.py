from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')

@app.route('/send_data', methods=['POST'])
def send_data():
    robot_type = request.form['robot_type']
    robot_id = request.form['robot_id']
    command = request.form['command']
    argument_1 = request.form['argument_1']
    argument_2 = request.form['argument_2']
    argument_3 = request.form['argument_3']
    
    data = {
        'robot_type': robot_type,
        'robot_id': robot_id,
        'command': command,
        'argument_1': argument_1,
        'argument_2': argument_2,
        'argument_3': argument_3
    }
    try:
        response = requests.post('http://127.0.0.1:5011/receive_data', json= data)
        if response.status_code == 200:
            return 'Data sent successfully!'
        else:
            return 'Failed to send data.'
    except requests.exceptions.RequestException as e:
        return f'Error sending data: {e}'

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5010)

