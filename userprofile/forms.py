from django import forms
from django.forms import ModelForm
from .models import Book

# AddBooks form
GENRE_CHOICES =[
    ("science fiction", "science fiction"), 
    ("fantasy", "fantasy"), 
    ("romance", "romance"), 
    ("dystopian", "dystopian"),
    ("action and adventure", "action and adventure"),
    ("mystery", "mystery"),
    ("horror", "horror"),
    ("historical fiction", "historical fiction"),
    ("graphic novel", "graphic novel"),
    ("classic", "classic"),
]

NOOK_CHOICES =[
    ("Select Nook Address", "Select Nook Address"),
    ("Monroe Township Library", "Monroe Township Library"),
    ("East Brunswick Public Library", "East Brunswick Public Library"),
    ("North Brunswick Public Library", "North Brunswick Public Library"),
    ("Metuchen Public Library", "Metuchen Public Library"),
]

class AddBooksForm(ModelForm):
    class Meta:
        model = Book

        fields = ('title', 'author', 'min_age', 'genre', 'location', 'rating')

        labels = {
            'title':'',
            'author':'',
            'min_age':'',
            'genre':'',
            'location':'',
            'rating':'',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Book Title'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author'}),
            'min_age': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Minimum Recommended Age'}),
            'genre': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Genre'},choices=GENRE_CHOICES),
            'location': forms.Select(attrs={'class':'form-control', 'placeholder':'Nook Address'},choices=NOOK_CHOICES),
            'rating': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Rating (1-5)'}),
        }

class CheckOutForm(forms.Form):
    fields = ()

    labels = {
        '':"",
    }