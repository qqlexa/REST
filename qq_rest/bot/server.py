import socket
import asyncio


class Server:
    def __init__(self, name="server", ip=None, port=None):
        self.name = name
        self.ip = ip
        self.port = port
        self.sock = socket.socket()
        self.conn = None
        self.addr = None
        self.accept_status = False
        self.connected = False

    def create_server(self):
        try:
            self.sock.bind((self.ip, self.port))
            self.sock.listen(1)
        except BaseException:
            print("There is problem with creating of server "
                  "`{ip}:{port}`!".format(ip=self.ip, port=self.port))
            return False
        else:
            self.connected = True
            print("Created!")
            return True

    def accept(self):
        if not self.accept_status:
            self.accept_status = True
            try:
                self.conn, self.addr = self.sock.accept()
                print("Connected from `{ip}:{port}`!".format(ip=self.addr[0], port=self.addr[1]))
            except BaseException:
                print("There is problem with accepting to "
                      "`{ip}:{port}`!".format(ip=self.ip, port=self.port))

    def close(self):
        self.sock = socket.socket()
        self.connected = False
        self.accept_status = False

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
            packet = self.conn.recv(size)
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

