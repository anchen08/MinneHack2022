from django import forms

class InputForm(forms.Form):
    fname = forms.CharField(label='First Name', max_length=50)
    mname = forms.CharField(label='Middle Name', max_length=50)
    lname = forms.CharField(label='Last Name', max_length=50)
    phone = forms.CharField(label='Phone Number', max_length=11)
    email = forms.CharField(label='Email', max_length=62)
    zip = forms.CharField(label='Zipcode', max_length=15)

