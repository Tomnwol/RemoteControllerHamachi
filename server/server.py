import socket
import keyboard

HOST = "25.41.206.132"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"Serveur UDP en écoute sur {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    commande = data.decode("utf-8")
    print(f"Commande reçue de {addr}: {commande}")
    if commande == "z":
        keyboard.press("z")
        keyboard.wait(0.1)
        keyboard.release("z")
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