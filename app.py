from socketIO_client import SocketIO, BaseNamespace
import logging
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()

# class DrawNamespace(BaseNamespace):
#
#     def on_draw_response(self, *args):
#         print('DRAW', args)

class ConnectNamespace(BaseNamespace):

    def on_connect_response(self, *args):
        print('CONNECT', args)

    # def on_disconnect_response(self, *args):
    #     print('DISCONNECT', args)

socketIO = SocketIO(host='localhost', port=5000)
print('Client running...')

connect_namespace = socketIO.define(ConnectNamespace, '/connect')
# draw_namespace = socketIO.define(DrawNamespace, '/draw')
print ('Namespaces defined.')

connect_namespace.emit('connect', 'I want to connect')
# draw_namespace.emit('draw', 'square')
socketIO.wait(seconds=3)
