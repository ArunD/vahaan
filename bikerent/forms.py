from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bikerent.models import BikeDetail

#from password_reset.forms import PasswordRecoveryForm,PasswordResetForm
from django.contrib.auth.forms import PasswordResetForm

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.email(self.cleaned_data["email"])
            if commit:
                user.save()
            return user

class BikeSelectForm(UserCreationForm):
    vehicle_name = forms.CharField(required=True)
    is_active = forms.IntegerField(required=True)

    class Meta:
        model = BikeDetail
        fields = ('vehicle_name','is_active')


class MyPasswordRecoveryForm(PasswordResetForm):
    #username_or_email = forms.CharField(label=("Username or Email"))
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        #fields = ('username','email')
        fields = ('email')
    #email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)
