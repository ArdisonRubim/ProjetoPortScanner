import socket  #Biblioteca para trabalhar com a placa de rede

ip = input("Digite o HOST ou IP para verificacao: ")

ports = []  # Vetor para receber as portas
count = 0   # Definindo contador

while count < 10:
    ports.append(int(input("Digite a porta a ser verificada: ")))
    count +=1

for port in ports:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.05) # Definindo tempo de resposta TCP
    code = cliente.connect_ex((ip,port))

    if code == 0:
        print(str(port), " -> Porta Aberta")
    else:
        print(str(port), " -> Porta Fechada")
print("Scan Fizalizado com sucesso! ")