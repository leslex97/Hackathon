from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
    email = forms.EmailField()
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Numer telefonu podaj w formacie : '+999999999'. Dozwolone 9 do 12 cyfr.")
    telefon = forms.CharField(validators=[phone_regex], max_length=17)
    
    class Meta:
        model = User
        fields = ['username','password1','password2','email','telefon']