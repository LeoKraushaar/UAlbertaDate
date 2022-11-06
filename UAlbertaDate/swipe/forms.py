from django import forms

class LikeForm(forms.Form):
    liked = forms.BooleanField()

class PassForm(forms.Form):
    passed = forms.BooleanField()