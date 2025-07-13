import os
from PIL import Image

zoom_factor = 1.15  # facteur de zoom
final_size = (300, 300)  # taille finale

for dossier in os.listdir("."):
    if os.path.isdir(dossier):
        image_path = os.path.join(dossier, "0.png")
        if os.path.exists(image_path):
            img = Image.open(image_path).convert("RGBA")
            largeur, hauteur = img.size

            # Étape 1 : Zoom 1.5
            new_width = int(largeur * zoom_factor)
            new_height = int(hauteur * zoom_factor)
            img_zoom = img.resize((new_width, new_height), Image.LANCZOS)

            # Étape 2 : Recadrage pour centrer le zoom
            left = (new_width - largeur) // 1.5
            top = (new_height - hauteur) // 1.5
            right = left + largeur
            bottom = top + hauteur
            img_cropped = img_zoom.crop((left, top, right, bottom))

            # Étape 3 : Redimensionner en 512x512
            img_final = img_cropped.resize(final_size, Image.LANCZOS)

            # Étape 4 : Sauvegarde PNG compressé
            img_final.save(
                image_path,
                format="PNG",
                optimize=True,
                compress_level=9
            )

            print(f"✅ {image_path} zoomé ×1.5 et redimensionné en 512x512")
        else:
            print(f"⚠️ {image_path} introuvable")
