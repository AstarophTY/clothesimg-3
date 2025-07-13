
import os
from PIL import Image

# Paramètres d'optimisation
MAX_SIZE = (800, 800)  # Résolution maximale (largeur, hauteur)
QUALITY = 85  # Qualité de compression (0-100)

def optimize_image(image_path):
    try:
        with Image.open(image_path) as img:
            # Redimensionner si nécessaire
            img.thumbnail(MAX_SIZE, Image.LANCZOS)
            # Sauvegarder avec optimisation
            img.save(image_path, optimize=True, quality=QUALITY)
            print(f"Optimisé : {image_path}")
    except Exception as e:
        print(f"Erreur avec {image_path} : {e}")

def optimize_all_images(root_dir):
    for folder in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder)
        if os.path.isdir(folder_path):
            img_path = os.path.join(folder_path, "0.png")
            if os.path.isfile(img_path):
                optimize_image(img_path)

if __name__ == "__main__":
    optimize_all_images(os.getcwd())
