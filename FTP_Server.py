from cgitb import handler
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os,socket
IP=socket.gethostbyname(socket.gethostname())
PATH='C:\\FTP'
os.chdir(PATH)
#FTP Server IP and wich port (21)
address=(IP,21)
authorizer = DummyAuthorizer()
authorizer.add_user('admin','adminpass','.',perm='elardfmw')

handler=FTPHandler
handler.authorizer = authorizer
server = FTPServer(address,handler)
server.serve_forever()
