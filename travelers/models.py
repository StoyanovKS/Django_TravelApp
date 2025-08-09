from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.db import models

class Traveler(models.Model):
    nickname = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            MinLengthValidator(3),
            RegexValidator(r"^[A-Za-z0-9]+$", message="Your nickname is invalid!"),
        ],
        help_text="*Nicknames can contain only letters and digits.",
    )
    email = models.EmailField(max_length=30, unique=True)
    country = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3), MaxLengthValidator(3)],
    )
    about_me = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nickname
