from PIL import Image
from pyzbar.pyzbar import decode

def decode_qr(image_path):
    # Ouvrir l'image
    image = Image.open(image_path)

    # Décoder le QR code à partir de l'image
    decoded_objects = decode(image)
    
    # Extraire et retourner le texte du QR code
    if decoded_objects:
        qr_text = decoded_objects[0].data.decode('utf-8')
        return qr_text
    else:
        return "Aucun QR code détecté"

# Chemin vers l'image du QR code
image_path = 'generatedQrCode.png'

# Décoder le texte du QR code et l'afficher
qr_text = decode_qr(image_path)
print(qr_text)
