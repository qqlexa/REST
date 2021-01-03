import socket
import asyncio


class Client:
    def __init__(self, name="client", ip=None, port=None):
        self.name = name
        self.ip = ip
        self.port = port
        self.client = None

    def connect(self):
        try:
            self.client = socket.socket()
            self.client.connect((self.ip, self.port))
        except BaseException:
            print("There is problem with connecting to "
                  "`{ip}:{port}`!".format(ip=self.ip, port=self.port))
            return False
        else:
            print("Connected to `{ip}:{port}`!".format(ip=self.ip, port=self.port))
            return True

    def send(self, packet=b'0', s_type="b"):
        try:
            if s_type == "t":
                packet = packet.encode("utf-8")
            self.conn.send(packet)
        except BaseException:
            print("Problem with sending!")
            return False
        else:
            print("Sent!")
            return True

    def recv(self, size=1024, s_type="b"):
        try:
            packet = self.client.recv(size)
            if s_type == "t":
                packet = packet.decode("utf-8")
            return packet
        except BaseException:
            print("Problem with getting!")
            return False

    def print_name(self):
        print(self.name)

    def print_ip(self):
        print(self.ip)

    def print_port(self):
        print(self.port)

    def print_info(self):
        """
        :print: all info
        """

        self.print_name()
        self.print_ip()
        self.print_port()

