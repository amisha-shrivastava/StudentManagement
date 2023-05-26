from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    profile_pic = forms.ImageField()
    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female')))
    course_preferences = forms.CharField(widget=forms.Textarea)
