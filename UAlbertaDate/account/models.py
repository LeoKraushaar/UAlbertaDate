from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    
    # Key to link to User object
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        )
    
    image_file = models.ImageField(
        null=True,
        blank=True
        )

    # Physical Attributes
    height_ft = models.IntegerField()
    height_in = models.IntegerField()
    
    # Mating Goals
    looking_for = models.CharField(max_length=40)
    target_gender = models.CharField(max_length=40)

    # School-based
    major = models.CharField(max_length=40)
    year_of_study = models.IntegerField()
    most_hated_course = models.CharField(max_length=40)

    # Other
    first_name = models.CharField(max_length=40, null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=40)
    hometown = models.CharField(max_length=50)
    bio = models.TextField(max_length=300)

    def get_attributes(self):
        attrs = [
            str(self.height_ft)+"'"+str(self.height_in),
            self.looking_for,
            self.major,
            self.year_of_study,
            self.most_hated_course,
            self.age,
            self.gender,
            self.hometown,
            self.bio
        ]

        labels = [

            "Height: ",
            "Looking for: ",
            "Major: ",
            "Year of study: ",
            "Most hated course: ",
            "Age: ",
            "Gender: ",
            "Hometown: ",
            "Bio: "
        ]

        return dict(zip(labels, attrs))

    def get_image_url(self):
        return "http://127.0.0.1:8000/static/media/{}".format(self.image_file)