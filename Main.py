import proxylib
import logging
import time
import socketserver
import socket
import sys

HOST, PORT = '0.0.0.0', 5060

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname_ex(socket.gethostname())[2][0]
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    proxylib.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    proxylib.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    with socketserver.UDPServer((HOST, PORT), proxylib.UDPHandler) as server:
        server.serve_forever()
