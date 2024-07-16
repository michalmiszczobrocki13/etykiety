import qrcode
import os
from PIL import Image

class qr_code:
    def __init__(self, cmms_input):
        self.cmms_input = cmms_input

    def generate_qr(self):
        # Generowaie QR
        qr = qrcode.QRCode(
            version=1,  # wersja kodu QR (rozmiar)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # poziom korekcji błędów
            box_size=5,  # rozmiar każdego kwadratu w kodzie QR
            border=1,  # szerokość obramowania kodu QR
        )

        # Dodajemy dane do kodu QR
        qr.add_data(self.cmms_input)
        qr.make(fit=True)
        print("Qr jest generowany")

        # Tworzymy obrazek kodu QR
        img = qr.make_image(fill='black', back_color='white')

        # Zapisujemy obrazek kodu QR do pliku
        img.save("QR.png")

    def clear_png(self):
        if os.path.isfile("QR.png"):
            os.remove("QR.png")
            print(f"plik: 'QR.png' został usnunięty")
        else:
            print(f"nie znaleziono pliku do usunięcia: 'QR.png'")


