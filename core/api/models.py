from django.db import models

class UserModel(models.Model):

    token = models.TextField(
        default=""
    )
