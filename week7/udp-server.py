from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("[SYSTEM] Server siap digunakan")

running = True
while running:
    connectionSocket, clientAddress = serverSocket.accept()
    print(f"[SYSTEM] Terhubung dengan {clientAddress[0]}:{clientAddress[1]}")

    while True:
        message = connectionSocket.recv(2048)

        if not message:
            break

        # Mendekode pesan
        original_message = message.decode().strip()

        # Cek apakah pesan adalah perintah keluar
        if original_message.lower() == 'exit':
            print("[SYSTEM] Mematikan server...")
            running = False
            break

        # Ubah ke huruf kapital
        modifiedMessage = original_message.upper()

        # Tampilkan info
        print(f"Diterima dari {clientAddress[0]}:{clientAddress[1]}: {original_message}")
        print(f"Mengirim balik: {modifiedMessage}")

        # Kirim kembali ke client (TCP → pakai send, bukan sendto)
        connectionSocket.send(modifiedMessage.encode())

    connectionSocket.close()

serverSocket.close()
print("[SYSTEM] Server ditutup")