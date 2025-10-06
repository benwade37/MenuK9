from django import forms
from .models import Recipe
import cloudinary.uploader

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'image', 'status']  # Include 'status'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'For example: The Guvnors Gravy'
                }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3,
                'placeholder': 'For example: This is a gravy recipe tweaked for dogs, packed with vitamins for a healthy coat and joints'
                }),
            'steps': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 10,
                'placeholder': 'Step 1: Take out small bones and skin \nStep 2: Mix ingredients \nStep 3: Simmer for 2 hours \nEtc'}),
            'status': forms.Select(attrs={'class': 'form-control'})  # Dropdown for status
        }
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 5 * 1024 * 1024:  # 5 MB limit
            raise forms.ValidationError("Image file size must be less than 5 MB.")
        if image:
            result = cloudinary.uploader.upload(image)
            print(result)  # Should return the uploaded file's details
        return image
