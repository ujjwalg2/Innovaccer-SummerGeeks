from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=200)
    contact = models.CharField(max_length = 10)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Host(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    offline = models.BooleanField(default = False)

    def __str__(self):
        return self.user.email

class Visitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE, null=True)
    checkIn = models.DateTimeField('checkIn time')
    checkOut = models.DateTimeField('checkOut time', null=True)

    def __str__(self):
        return self.user.email