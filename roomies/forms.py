from django import forms
class RegistrationForm(forms.Form):
    username = forms.EmailField(max_length=30, widget=forms.TextInput(attrs=attrs_dict))
    password1 = forms.PasswordField()
    password2 = forms.PasswordField()
    first_name = forms.CharField(max_length=100)