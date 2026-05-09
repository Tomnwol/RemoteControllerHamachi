import socket
import keyboard

HOST = "25.xxx.xxx.xxx"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"Serveur UDP en écoute sur {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    commande = data.decode("utf-8")
    print(f"Commande reçue de {addr}: {commande}")
    if commande == "z":
        keyboard.press_and_release("z")
        print("AVANCER")

    elif commande == "s":
        keyboard.press_and_release("s")
        print("RECULER")

    elif commande == "q":
        keyboard.press_and_release("q")
        print("GAUCHE")

    elif commande == "d":
        keyboard.press_and_release("d")
        print("DROITE")