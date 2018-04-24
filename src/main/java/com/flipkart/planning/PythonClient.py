import sys
sys.path.append('gen-py')

from helloworld import HelloWorld
from helloworld.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HelloWorld.Client(protocol)
    transport.open()
    client.sayMsg("Hey Baby Drop it Down, Just wanna see you hit the Ground!!")

    client.assignValue("x","23")
    client.assignValue("y","3")

    value1 = client.getValue("x")
    value2 = client.getValue("y")
    print value1,value2

    client.execScript("test")

    transport.close()

except Thrift.TException, tx:
  print "%s" % (tx.message)