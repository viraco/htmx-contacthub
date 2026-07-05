from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='contacts')  # related_name allows querying like users.contacts.all()

    class Meta:
        unique_together = ('user', 'email')  # adds a constraint to ensure uniqueness of email per user

    def __str__(self):
        return f"{self.name} <{self.email}>"
