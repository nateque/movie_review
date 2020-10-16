from django import forms
from .models import *

# movie add form
class MovieForm(forms.ModelForm):
    release_date = forms.DateField(widget= forms.DateInput(attrs= {
        'placeholder': 'YYYY-MM-DD',
    }))

    image = forms.URLField(widget= forms.URLInput(attrs= {
        'placeholder': 'Paste your image url here...',
    }))

    class Meta:
        model = Movie
        fields = ('name', 'director', 'cast', 'description', 'release_date', 'image')
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")