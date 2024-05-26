import qrcode
from PIL import Image

# 1. Créer un objet QRCode avec des configurations spécifiques
qr = qrcode.QRCode(
    version=1,  # Contrôle la taille du QR code (de 1 à 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveau de correction d'erreur
    box_size=10,  # Taille de chaque case en pixels
    border=4,  # Taille de la bordure en cases
)

# 2. Ajouter des données au QR code
qr.add_data(' adachi mohammed')
qr.make(fit=True)  # Ajuste les dimensions du QR code pour s'adapter aux données

# 3. Créer une image du QR code
img = qr.make_image(fill_color='black', back_color='white')

# 4. Sauvegarder l'image du QR code dans un fichier
img_path = 'qrcode.jpg'
img.save(img_path)

# 5. Convertir l'image en une représentation ASCII
def image_to_ascii(image_path):
    # Ouvrir l'image
    image = Image.open(image_path)
    image = image.convert('L')  # Convertir en niveaux de gris

    # Redimensionner l'image (facultatif, pour ajuster la taille dans la console)
    width, height = image.size
    aspect_ratio = height / width
    new_width = 100  # Vous pouvez ajuster cette valeur
    new_height = int(aspect_ratio * new_width * 0.55)
    image = image.resize((new_width, new_height))

    # Définir les caractères ASCII pour les niveaux de gris
    ascii_chars = "@%#*+=-:. "

    # Convertir les pixels de l'image en caractères ASCII
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ascii_chars[pixel // 32]  # Diviser par 32 pour réduire les 256 niveaux de gris en 8 niveaux

    # Regrouper la chaîne en lignes correspondant à la largeur de l'image
    ascii_lines = [ascii_str[index:index + new_width] for index in range(0, len(ascii_str), new_width)]
    ascii_image = "\n".join(ascii_lines)

    return ascii_image

# Convertir et afficher le QR code en ASCII
ascii_qr_code = image_to_ascii(img_path)
print(ascii_qr_code)
