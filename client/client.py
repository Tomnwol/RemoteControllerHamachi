import socket
import keyboard

# IP Hamachi du serveur
SERVER_IP = "25.xxx.xxx.xxx"
PORT = 5005

# Création socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Client prêt.")
print("Touches : z q s d")
print("ECHAP pour quitter")

while True:

    # Quitter
    if keyboard.is_pressed("esc"):
        break

    # Touches
    for touche in ["z", "q", "s", "d"]:

        if keyboard.is_pressed(touche):

            # Envoi UDP
            sock.sendto(touche.encode("utf-8"), (SERVER_IP, PORT))

            print(f"Commande envoyée : {touche}")

            # évite le spam
            keyboard.wait(touche)