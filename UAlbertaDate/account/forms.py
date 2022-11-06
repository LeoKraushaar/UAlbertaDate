from django import forms
from .models import UserInfo as UserInfo

class PersonalInfoForm(forms.ModelForm):

    LOOKING_FOR_CHOICES = [
        (0, "Not sure yet"),
        (1, "Something short-term"),
        (2, "Something long-term")
    ]

    TARGET_GENDER_CHOICES = [
        (["m"], "Men"),
        (["f"], "Women"),
        (["m", "f"], "Men and Women"),
        (["all"], "Anything")
    ]

    FACULTY_CHOICES = [
        ("kin", "Kinesiology/Sport + Recreation"),
        ("med", "Medicine/Dentistry"),
        ("nurs", "Nursing"),
        ("phar", "Pharmaceutical Sciences"),
        ("rehab", "Rehabilitation Medicine"),
        ("agg", "Agriculture/Environmental Sciences"),
        ("engg", "Engineering"),
        ("sci", "Science"),
        ("bus", "Business"),
        ("art", "Arts/Humanities"),
        ("edu", "Education"),
        ("law", "Law")
    ]

    MAJOR_CHOICES = [              # Incomplete
        ("bio", "Biological Sciences"),
        ("chem", "Chemistry"),
        ("comp", "Computer Science"),
        ("math", "Mathetmatics/Statistics"),
        ("phys", "Physics"),
        ("psych", "Psychology"),
        ("mus", "Music")
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

    # image_file = forms.ImageField(
    #     allow_empty_file=True,
    #     required=False
    # )

    looking_for = forms.IntegerField(
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
        widget=forms.RadioSelect(
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
        fields = "__all__"