from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Advisor(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    profile_pic = models.ImageField()
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=30,null=True)
    password = models.CharField(max_length=100,null=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    advisor_id = models.ForeignKey(Advisor, to_field='id', on_delete=models.CASCADE)
    booking_id = models.ForeignKey(Customer, to_field='id', on_delete=models.CASCADE)
    booking_time = models.DateTimeField()


    def __str__(self):
        return str(self.booking_time)









