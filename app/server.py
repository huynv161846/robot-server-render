from flask import Flask, request
from flask import render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123456'
sio = SocketIO(app)

@app.route('/')
def main():
    request_data = request.get_json()
    print(request_data)
    return render_template(
        'index.html'
    )

@app.route('/run')
def request_run():
    print('Request taken')
    sio.emit('run')
    return "zzzz"

@sio.on('connect')
def connect():
    print('New client connected')
    request_run()
