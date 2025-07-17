from .models import Recipe, Comment, Baker
from django import forms
from django_summernote.widgets import SummernoteWidget
from cloudinary.forms import CloudinaryFileField


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'ingredients', 'instructions',
                  'time_required', 'categories', 'excerpt']
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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Baker
        fields = ['bio', 'profile_pic', 'user_type']
        widgets = {
            'bio': SummernoteWidget(),
            'profile_pic': CloudinaryFileField().widget,
        }
        labels = {
            'bio': 'Biography (A little about yourself)',
            'profile_pic': 'Profile Picture',
            'user_type': 'User Type',
        }