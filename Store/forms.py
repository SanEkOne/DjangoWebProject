from django import forms
from django.core.validators import MinLengthValidator
import os
from .models import ProductApplication

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductApplication
        fields = ['title', 'description', 'price', 'image']
        labels = {
            'title': 'Product Name',
            'description': 'Product Description',
            'price': 'Product Price',
            'image': 'Product Image',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        help_texts = {
            'image': "Разрешено: JPG, JPEG, PNG (максимум 5 МБ)",
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Изображение слишком большое. Максимальный размер — 5 МБ.")
        return image
