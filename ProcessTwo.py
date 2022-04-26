from mimetypes import init
import socket


class ProcessTwo:
  def __init__(self):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.conexao = None
  
  def validate_message(self, data_msg):
    response = None
    print(data_msg)
    if (len(data_msg) > 1):
      code = int(data_msg[0])
      n = int(data_msg[1])

      if ((code) > 10000000):
        if (n <= 15000 and n > 5000 ):
          response = data_msg[0] + "&" + data_msg[1]
        else:
          response = "Error: Invalid n -> 5000 < n < 15000"
      else:
        response = "Error: Invalid code - > code > 1000000"
    else:
      response = "Error: Number of args is invalid"
    
    return response

  def wait_response(self, socket):
    while (True):
      dados = socket.recv(1024)
      if (dados):
        print(f"Resposta do servidor: {dados.decode()}")
        return dados.decode()

  def get_message(self):
     while (True):
      data = self.conexao.recv(1024)
      if (data):
        decoded_message = data.decode()
        print(f"Mensagem recebida: {decoded_message}")
        inputs = decoded_message.split("&")

        response = self.validate_message(inputs)


        if "Error" in response:
          self.conexao.sendall(bytes(response, encoding='utf-8'))
        else:
          with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_s:
            socket_s.connect((socket.gethostname(), 4003))
            socket_s.sendall(bytes(response, encoding='utf-8'))
            response_process_3 = self.wait_response(socket_s)
            self.conexao.sendall(bytes(response_process_3, encoding='utf-8'))
        break
      

  def wait_client(self):
    self.s.bind((socket.gethostname(), 4002))
    print(self.s)
    self.s.listen()
    while True:
      self.conexao, addr = self.s.accept()
      print(f"Cliente conectado: {addr}")
      self.get_message()
