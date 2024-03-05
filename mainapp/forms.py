from django import forms

class WeatherForm(forms.Form):
    city = forms.CharField(label='City')
    email = forms.EmailField(label='Email')
