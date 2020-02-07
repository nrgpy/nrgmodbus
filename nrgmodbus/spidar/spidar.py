#!/bin/usr/python
from .registers import spidar_registers

class spidar_v1(object):
    """ """
    def __init__(self, ip='', port=502, unit=1, connect=False):
        self.ip = ip
        self.port = port
        self.unit = unit
        self.init_registers()
        self.e = ''
        if connect == True:
            self.connect()

    def init_registers(self):
        self.hr = spidar_registers()

    def connect(self):
        """
        initialize self.ip, self.port, self.unit
        """
        from pymodbus.client.sync import ModbusTcpClient as ModbusClient

        self.client = ModbusClient(host=self.ip,port=self.port,unit=self.unit)
        print("Connecting to {0}... \t\t".format(self.ip), end="", flush=True)
        try:
            self.client.connect()
            if self.client.is_socket_open() == True:
                print("[OK]")
            else:
                self.client.connect()
                if self.client.is_socket_open != True:
                    raise ValueError('Could Not Connect to {0}'.format(self.ip))
        except Exception as e:
            self.e = e
            print("[FAILED]")
            print(self.e)

    def disconnect(self):
        print("Disconnecting from {0}... \t\t".format(self.ip), end="", flush=True)
        try:
            self.client.close()
            print("[OK]")
        except Exception as e:
            print("[ERROR]")
            print(e)