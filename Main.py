import bluetooth

# IPhone'ning MAC manzilini aniqlash
target_name = "iPhone"  # IPhone'ingizning nomi
target_address = None

devices = bluetooth.discover_devices()

for addr in devices:
    if target_name == bluetooth.lookup_name(addr):
        target_address = addr
        break

if target_address is not None:
    print("IPhone topildi. Bog'lanish urunildi.")
    # IPhone bilan bog'lanishni boshlash
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((target_address, 1))
    
    # Bog'lanishni sinab ko'rish
    try:
        sock.send("Assalomu alaykum, iPhone!")
        data = sock.recv(1024)
        print("iPhone javob qaytardi: ", data.decode())
    except bluetooth.btcommon.BluetoothError as error:
        print("Xatolik yuz berdi:", str(error))
    
    # Bog'lanishni yopish
    sock.close()
else:
    print("IPhone topilmadi.")