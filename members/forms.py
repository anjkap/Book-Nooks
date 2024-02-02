from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from userprofile.models import Profile

GENRE_CHOICES =[
    ("fiction", "fiction"), 
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

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1','password2',)

        labels = {
            'username':'',
            'password1':'',
            'password2':'',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a username'}),
            'password': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Password'}),
        }

class UserProfileForm(ModelForm):
    class Meta:
        model = Profile

        fields = ('fav_genres', 'age', 'bio')

        labels = {
            'age':'',
            'fav_genres':'Choose your favorite genre(s)',
            'bio':'',
        }

        widgets = {
            'age': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter your age'}),
            'fav_genres': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Genre'},choices=GENRE_CHOICES),
            'bio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your bio'}),
        }