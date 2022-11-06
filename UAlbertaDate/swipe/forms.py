from django import forms

class LikeForm(forms.Form):
    liked = forms.BooleanField(
        required=False
    )

class PassForm(forms.Form):
    passed = forms.BooleanField(
        required=False
    )