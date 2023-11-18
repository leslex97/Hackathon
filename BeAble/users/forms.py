from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django import forms
from users.models import Disabled_info


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
    imie = forms.CharField()
    nazwisko = forms.CharField()
    
    def clean_username(self):
        username = '0'
        return username
    
    ACCOUNT_TYPE= [
        ('1', 'Zdrowy'),
        ('2', 'Chroy'),
    ]
    rodzaj_konta = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=ACCOUNT_TYPE, 
    )
    
    
    email = forms.EmailField()
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Numer telefonu podaj w formacie : '+999999999'. Dozwolone 9 do 12 cyfr.")
    telefon = forms.CharField(validators=[phone_regex], max_length=17)
    
    class Meta:
        model = User
        fields = ['imie','nazwisko','email', 'password1','password2','telefon','rodzaj_konta']
        



class UserInfoForm(forms.Form):
    
    SEX_CHOICES= [
        ('1', 'Kobieta'),
        ('2', 'Mężczyzna')
    ]
    
    age = forms.IntegerField()
    city = forms.CharField(max_length=200)
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX_CHOICES)
    disability_type = forms.CharField(max_length=300)

    
        
    class Meta:
        model = Disabled_info
        fields = ['user','age','sex','city', 'disability_type']