def restore_image(image_path):
    backup_path = image_path + ".bak.png"
    if os.path.exists(backup_path):
        try:
            with Image.open(backup_path) as img:
                img.save(image_path)
            print(f"Restauré : {image_path}")
        except Exception as e:
            print(f"Erreur restauration {image_path} : {e}")
    else:
        print(f"Aucune backup trouvée pour : {image_path}")

def restore_all_images(root_dir):
    for folder in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder)
        if os.path.isdir(folder_path):
            img_path = os.path.join(folder_path, "0.png")
            if os.path.isfile(img_path):
                restore_image(img_path)

import os
from PIL import Image

# Paramètres d'optimisation
MAX_SIZE = (512, 512)  # Résolution maximale (largeur, hauteur)
QUALITY = 85  # Qualité de compression (0-100)


def backup_image(image_path):
    backup_path = image_path + ".bak.png"
    if not os.path.exists(backup_path):
        try:
            with Image.open(image_path) as img:
                img.save(backup_path)
            print(f"Backup créé : {backup_path}")
        except Exception as e:
            print(f"Erreur backup {image_path} : {e}")

def zoom_image(image_path, zoom_factor=1.2):
    try:
        with Image.open(image_path) as img:
            w, h = img.size
            new_w = int(w / zoom_factor)
            new_h = int(h / zoom_factor)
            left = (w - new_w) // 2
            top = (h - new_h) // 2
            right = left + new_w
            bottom = top + new_h
            img_cropped = img.crop((left, top, right, bottom)).resize((w, h), Image.LANCZOS)
            img_cropped.save(image_path)
            print(f"Zoom appliqué : {image_path}")
    except Exception as e:
        print(f"Erreur zoom {image_path} : {e}")

def optimize_image(image_path, zoom=False, zoom_factor=1.2):
    backup_image(image_path)
    if zoom:
        zoom_image(image_path, zoom_factor)
    try:
        with Image.open(image_path) as img:
            img.thumbnail(MAX_SIZE, Image.LANCZOS)
            img.save(image_path, optimize=True, quality=QUALITY)
            print(f"Optimisé : {image_path}")
    except Exception as e:
        print(f"Erreur avec {image_path} : {e}")


def optimize_all_images(root_dir, zoom=False, zoom_factor=1.2):
    for folder in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder)
        if os.path.isdir(folder_path):
            img_path = os.path.join(folder_path, "0.png")
            if os.path.isfile(img_path):
                optimize_image(img_path, zoom=zoom, zoom_factor=zoom_factor)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "restore":
        # Pour restaurer toutes les images depuis les backups
        restore_all_images(os.getcwd())
    else:
        # Pour activer le zoom, passer zoom=True
        optimize_all_images(os.getcwd(), zoom=True, zoom_factor=1.4)
