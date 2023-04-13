import socket

print(r"""
      
  #####                                  ######                       ##
 ##   ##                                       ##  ##                      ##
 #         ####     ####    #####              ##  ##   ####    ######    #####
  #####   ##  ##       ##   ##  ##   ######    #####   ##  ##    ##  ##    ##
      ##  ##        #####   ##  ##             ##      ##  ##    ##        ##
 ##   ##  ##  ##   ##  ##   ##  ##             ##      ##  ##    ##        ## ##
  #####    ####     #####   ##  ##            ####      ####    ####        ###

""")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("maiseletronicos.com.br", 22 )) # Escolha seu alvo e uma porta.
sock.send("teste\n".encode())
resposta = sock.recv(1024)
print(resposta)