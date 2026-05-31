from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'txt_field','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'txt_field','placeholder':'Password'}))

class RegistrationForm(forms.Form):
    patientNo = forms.CharField(max_length=20,widget=forms.TextInput)
    code= forms.CharField(max_length=20,widget=forms.TextInput)
    encounter=forms.CharField(max_length=20,widget=forms.TextInput)
    ptName=forms.CharField(max_length=50,widget=forms.TextInput)
    ptLastName=forms.CharField(max_length=50,widget=forms.TextInput)
    gender=forms.ComboField
    ageDate=forms.DateField
    ageYear=forms.NumberInput
    district=forms.ComboField
    address=forms.ComboField

