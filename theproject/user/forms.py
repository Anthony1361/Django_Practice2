from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):

    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'First Name', 'class': 'form-control'}),
    )

    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class': 'form-control'}),
    )

    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Username', 'class': 'form-control'}),
    )

    email = forms.EmailField(max_length=234,widget=forms.TextInput(attrs={'placeholder':'Email', 'class': 'form-control'}),
    )

    age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Age', 'class': 'form-control'}),
    )

    SKILL_CHOICES =[
        ('', 'CHOOSE SKILL'),
        ('teacher', 'Teacher'), ('musician', 'Musician')
    ]

    skill = forms.ChoiceField(choices=SKILL_CHOICES,widget=forms.Select(attrs={ 'class': 'form-control'}),
    )

    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={ 'class': 'form-control'}),
    )

    password1 = forms.CharField(max_length=30,label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class': 'form-control'}),
    )

    password2 = forms.CharField(max_length=30,label='Password Confirmation',widget=forms.PasswordInput(attrs={'placeholder':'Confirm password', 'class': 'form-control'}),
    )

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "email", "age", "skill", "profile_picture", "password1", "password2")