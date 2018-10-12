from socketIO_client import SocketIO, BaseNamespace

class DrawNamespace(BaseNamespace):

    def on_draw_response(self, *args):
        print('DRAW', args)

class ConnectNamespace(BaseNamespace):

    def on_connect_response(self, *args):
        print('CONNECT', args)

    def on_disconnect_response(self, *args):
        print('DISCONNECT', args)

socketIO = SocketIO('3139b29d.ngrok.io', 80)
print('Client running...')
connect_namespace = socketIO.define(ConnectNamespace, '/connect')
draw_namespace = socketIO.define(DrawNamespace, '/draw')

connect_namespace.emit('connect')
draw_namespace.emit('draw')
socketIO.wait(seconds=3)
