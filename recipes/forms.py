from django import forms
from .models import Recipe
from django_summernote.widgets import SummernoteWidget
from cloudinary.forms import CloudinaryFileField


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'ingredients', 'instructions',
                  'time_required', 'categories', 'excerpt'] # Include the image field
        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
            'image': CloudinaryFileField().widget,
        }
        labels = {
            'title': 'Title (Your Recipe Name)',
            'image': 'Image (Make it look delicious)',
            'ingredients': 'Ingredients (Be specific!)',
            'instructions': 'Instructions (Be detailed, use numbered steps)',
            'time_required': 'Time Required (e.g. 30 minutes)',
            'categories': 'Categories (Select all that apply)',
            'excerpt': 'Blurb (Short description of your recipe)',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {
            'comment': 'Comment',
        }
        help_texts = {
            'comment': 'Leave a comment',
        }


class LikeForm(forms.Form):
    pass

lass RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'image']  # Include the image field