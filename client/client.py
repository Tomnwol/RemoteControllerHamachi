import socket
import keyboard

SERVER_IP = "25.41.206.132"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Client prêt.")
print("Touches : z q s d")
print("ECHAP pour quitter")

while True:
    if keyboard.is_pressed("esc"):
        break
    for touche in ["z", "q", "s", "d"]:
        if keyboard.is_pressed(touche):
            sock.sendto(touche.encode("utf-8"), (SERVER_IP, PORT))

            print(f"Commande envoyée : {touche}")
            keyboard.wait(touche)