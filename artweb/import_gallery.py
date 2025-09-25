# scripts/import_gallery.py
import os
import shutil
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "artweb.settings")
django.setup()

from gallery.models import Gallery
from django.conf import settings

source_folder = os.path.join(settings.BASE_DIR, "artworks")
dest_folder = os.path.join(settings.MEDIA_ROOT, "gallery_images")
os.makedirs(dest_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(dest_folder, filename)
        shutil.copy2(src_path, dst_path)
        gallery = Gallery(
            image=f'gallery_images/{filename}',
            title=filename,
            description="รูปที่ import จาก artworks"
        )
        gallery.save()
        print(f'Imported {filename}')
