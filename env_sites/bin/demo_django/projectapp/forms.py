from django import forms

class InputForm(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    roll_number=forms.IntegerField(
            help_text="Enter 6 Digit roll number"
            )
    password=forms.CharField(widget=forms.PasswordInput())
