from socket import *

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("[SYSTEM] Masukkan pesan")

while True:
    message = input("> ")

    # Validasi jika input kosong
    if not message:
        continue

    # Kirim ke server
    clientSocket.send(message.encode())

    # Cek perintah keluar
    if message.lower() == "exit":
        print("Perintah exit dikirim. Menutup koneksi...")
        break
    elif message.lower() == "keluar":
        print("Menutup klien...")
        break

    try:
        # Terima balasan dari server
        modifiedMessage = clientSocket.recv(2048)
        print(f"[SERVER] {modifiedMessage.decode()}\n")
    except timeout:
        print("Kesalahan: Server tidak merespons (Timeout)\n")

clientSocket.close()
print("[SYSTEM] socket ditutup")