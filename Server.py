import socket
import time

host_ismi = "localhost"
port = 7777

internet_soketi = socket.socket()
internet_soketi.bind((host_ismi,port))
internet_soketi.listen(1)

bağlantı, adres = internet_soketi.accept()

print(str(adres)+" bağlantı sağlandı.")

while True:
    while True:
        try:
            gelen_veri = str(bağlantı.recv(1024).decode())
            print("client şunu yolladı :"+gelen_veri)
            break
        except ConnectionResetError:
            time.sleep(2)
            bağlantı,adres = internet_soketi.accept()
            print(str(adres)+" bağlantı sağlandı.")
    if gelen_veri == "çıkış":
        break
    else:
        mesaj = input("----::")
        print("client bekleniyor...")
        bağlantı.send(mesaj.encode())

bağlantı.close()
