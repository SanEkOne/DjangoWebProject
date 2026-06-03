import os
from django.db import models
from django.core.validators import MinLengthValidator
from datetime import datetime

def image_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    new_name = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"
    return f'images/{new_name}'

class ProductApplication(models.Model):
    title = models.CharField("Title", max_length=100, validators=[MinLengthValidator(1)])
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    description = models.TextField("Description", validators=[MinLengthValidator(1)])
    image = models.ImageField("Image", upload_to=image_upload_path, blank=True, null=True)

    created_at = models.DateTimeField("Дата відправки", auto_now_add=True)

    class Meta: 
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} — {self.created_at.strftime('%d.%m.%Y %H:%M')}"

