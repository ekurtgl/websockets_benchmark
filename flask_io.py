from flask import Flask, request
from flask_socketio import SocketIO
import socketio

class IOServer():

    def __init__(self):
        self.app = Flask(__name__)
        async_mode = None
        self.sio = SocketIO(self.app, async_mode=async_mode)

    def run(self):
        # self.sio.run(self.app, host='0.0.0.0', port=8080)
        self.sio.run(self.app, port=8000)

    def on(self, msg, handler):
        self.sio.on(msg)(handler)

    def send_msg(self, msg, data):
        self.sio.emit(msg, {'data': data})
    
    def recieve(self):
        data = request.get_data()
        return data
    
server = IOServer()

def onConnect():
    print('New Socket Connected')

def onDisconnect():
    print('Socket Disconnected')

def main():
    server = IOServer()
    server.on('connect', onConnect)
    server.on('disconnect', onDisconnect)
    server.run()


if __name__ == '__main__':
    main()