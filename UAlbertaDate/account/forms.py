from django import forms
from .models import UserInfo as UserInfo

class PersonalInfoForm(forms.ModelForm):

    LOOKING_FOR_CHOICES = [
        ("Not sure yet", "Not sure yet"),
        ("Something short-term","Something short-term"),
        ("Something long-term", "Something long-term"),
    ]

    TARGET_GENDER_CHOICES = [
        (["m"], "Men"),
        (["f"], "Women"),
        (["m", "f"], "Men and Women"),
        (["all"], "Anything")
    ]

    MAJOR_CHOICES = [
        ("Biological Sciences", "Biological Sciences"),
        ("Chemistry", "Chemistry"),
        ("Computer Science", "Computer Science"),
        ("Mathematics/Statistics", "Mathematics/Statistics"),
        ("Physics", "Physics"),
        ("Psychology", "Psychology"),
        ("Music", "Music"),
        ("Business", "Business"),
        ("Education", "Education"),
        ("Humanities", "Humanities")
    ]

    GENDER_CHOICES = [
        ("m", "Male"),
        ("f", "Female"),
        ("o", "Other")
    ]

    user = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )

    looking_for = forms.CharField(
        widget=forms.RadioSelect(
            choices=LOOKING_FOR_CHOICES
        )
    )

    target_gender = forms.CharField(
        widget=forms.RadioSelect(
            choices=TARGET_GENDER_CHOICES
        )
    )

    major = forms.CharField(
        widget=forms.Select(
            choices=MAJOR_CHOICES
        )
    )  

    gender = forms.CharField(
        widget=forms.RadioSelect(
            choices=GENDER_CHOICES
        )
    )

    class Meta:
        model = UserInfo
        exclude = [
            "first_name"
        ]