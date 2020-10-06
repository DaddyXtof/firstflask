# __init__.py makes the folder (application) behave like a package/modulde
from flask import Flask
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)
    print ("Something is happening")

from application import routes