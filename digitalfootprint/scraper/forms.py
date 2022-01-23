from django import forms

class InputForm(forms.Form):
    fname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}), label="", max_length=50)
    mname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Middle Name'}), label="", max_length=50)
    lname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}), label="", max_length=50)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone Number'}), label="", max_length=11)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}), label="", max_length=62)
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}), label="", max_length=100)
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'State'}), label="", max_length=100)
    zip = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Zipcode'}), label="", max_length=15)
