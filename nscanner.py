import nmap

scanner = nmap.PortScanner()

print("Seja vem vindo")
print("----------------")


ip = input("Digite o ip a ser varrido: ")
print("Voce digitou ", ip)
type(ip)

menu = input("""\n Escolha o tipo de varredura 
                1 -> Varredura do tipo SYN
                2 -> Varredura do tipo UDP
                3 -> Varredura do tipo INTENSA
                -------------------------------
                Digite a opcao escolhida: """)

print("Voce escolheu: ", menu)

if menu == "1":
    print("Versao do nmap: ", scanner._nmap_version_number())
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())
elif menu == "2":
    print("Versao do nmap: ", scanner._nmap_version_number())
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['udp'].keys())    
elif  menu == "3":
    print("Versao do nmap: ", scanner._nmap_version_number())
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())
else:
    print("Opcao inválida!")