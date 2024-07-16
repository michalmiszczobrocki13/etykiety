import os
from pathlib import Path
from ftplib import FTP


def test():
    print("test")


def upload_file_via_ftp(server, username, password, local_file_path, remote_file_path):
    try:
        # Utworzenie obiektu sesji FTP
        ftp = FTP(server)

        # Logowanie na serwerze FTP
        ftp.login(username, password)

        # Wysłanie pliku na serwer FTP
        with open(local_file_path, 'rb') as file:
            ftp.storbinary('STOR ' + remote_file_path, file)

        # Wylogowanie i zamknięcie sesji FTP
        ftp.quit()

        print("Plik został pomyślnie przesłany na serwer FTP.")
        print("Etykieta została wydrukowana")
    except Exception as e:
        print("Wystąpił błąd podczas przesyłania pliku:", str(e))


def drukuj(numer_cmms_in):
    try:
        numer_cmms = numer_cmms_in.replace("_", "-")

        numer_cmms = numer_cmms.upper()
        cmms_hex = ("#" + numer_cmms).encode().hex()
        # print(cmms_hex)
        text_file_content = (f"^XA\n"
                             "^PR3,3 \n"
                             "~SD28\n"
                             "^RS8,,,3\n"
                             # "^XZ\n"
                             # "^XA \n"
                             f"^FO80,100^A0N,55^FD{numer_cmms}^FS \n"
                             f"^FO330,60^BQN,3,6,M^FDLA,{numer_cmms}^FS\n"
                             "^RFW,H,1,2,1^FD3000^FS\n"
                             f"^RFW,H,2,8,1^FD{cmms_hex}0d0a0d0a0d0a^FS \n"
                             "^XZ")

        # TWORZENIE PLIKU
        downloads_path = str(Path.home()) + '\\Downloads'
        filepath = os.path.join(downloads_path, numer_cmms + ".zpl")
        f = open(filepath, "w")
        f.write(text_file_content)
        f.close()

        # Przykładowe użycie funkcji
        server = "10.74.93.12"
        username = "root"
        password = ""  # nie ma hasła
        local_file_path = filepath
        remote_file_path = f"{numer_cmms}.zpl"  # Ścieżka na serwerze, gdzie chcesz zapisać plik

        # upload_file_via_ftp(server, username, password, local_file_path, remote_file_path)
        print("wyslano")

        os.remove(filepath)

    except Exception as e:
        print("Podano nieprawidłowy numer CMMS:", str(e))
