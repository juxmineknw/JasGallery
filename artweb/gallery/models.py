from django.db import models

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')   # เก็บไฟล์รูป
    title = models.CharField(max_length=200)                 # ชื่อรูป
    description = models.TextField(blank=True, null=True)    # รายละเอียดรูป

    def __str__(self):
        return self.title
