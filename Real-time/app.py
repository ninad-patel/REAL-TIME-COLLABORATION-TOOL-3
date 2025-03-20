from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

document_content = {
    'text': ''
}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    # Send the current document content to the newly connected user
    emit('text_update', document_content)

@socketio.on('update_text')
def handle_text_update(data):
    # Update the document content and broadcast it to all users
    document_content['text'] = data['text']
    emit('text_update', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
