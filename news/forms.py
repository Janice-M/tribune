from django import forms


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name Rafiki :)',max_length=30)
    email=forms.EmailField(label='Enter Email Rafiki :)')
    
        