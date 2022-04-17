from mimetypes import init
import socket

class ProcessOne:
  def __init__(self, code="1000001", n="15000"):
    self.code = code
    self.n = n
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


  def send_message(self):
    self.s.connect((socket.gethostname(), 4002))
    print(self.s)
    message = self.code + "&" + self.n
    self.s.sendall(bytes(message, encoding='utf-8'))

  def wait_callback(self):
    while (True):
      dados = self.s.recv(1024)
      if (dados):
        decoded_message = dados.decode()
        msg = decoded_message.split("&")

        print(f"Key: {msg[0]}")
        print(f"Tempo: {msg[1]}")
        break