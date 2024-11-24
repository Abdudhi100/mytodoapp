from django import forms

class MyForm(forms.Form):
    fieldname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    report = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
