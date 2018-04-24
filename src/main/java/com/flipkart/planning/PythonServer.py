import sys
sys.path.append('gen-py')

from helloworld import HelloWorld
from helloworld.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class HelloWorldHandler:
    def __init__(self):
        self.log = {}

    def assignValue(self, variable, value):
        exec("globals()[variable] = value")

    def getValue(self, variable):
        return eval(variable)

    def execScript(self, scriptName):
        exec("import " + eval('scriptName'))
        exec('scriptName')

    def sayMsg(self, msg):
        print msg


if __name__ == '__main__':
    handler = HelloWorldHandler()
    processor = HelloWorld.Processor(handler)
    transport = TSocket.TServerSocket(host="localhost",port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print "Starting python server..."
    server.serve()
    print "done!.."