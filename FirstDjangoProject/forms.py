from django import forms

class practiceforms(forms.Form):
    firstName = forms.CharField(max_length=30, label="First Name:", widget=forms.TextInput(attrs={'class': "form-control"}))
    lastName = forms.CharField(max_length=30, label="Last Name:", widget=forms.TextInput(attrs={'class': "form-control"}))
    sureName = forms.CharField(max_length=30, label="Sure Name:", widget=forms.TextInput(attrs={'class': "form-control"}))