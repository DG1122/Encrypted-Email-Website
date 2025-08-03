from django.db import models
from Guest.models import *
# Create your models here.

class tbl_wishlist(models.Model):
    mail = models.ForeignKey(tbl_mail, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)