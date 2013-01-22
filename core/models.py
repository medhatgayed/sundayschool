from django.db import models

# Create your models here.

class Contact(models.Model):
    landline = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    emaiil = models.EmailField(blank=True)


class Servant(models.Model):
    name = models.CharField(max_length=255)
    contact = models.ForeignKey(Contact)
    sunday_school_class = models.CharField(max_length=255)
    book = models.CharField(max_length=255)


class Child(models.Model):
    name = models.CharField(max_length=255)
    contact = models.ForeignKey(Contact)
    dob = models.DateField(blank=True)
    school_year = models.PositiveSmallIntegerField()
    sunday_school_class = models.CharField(max_length=255)


class ServantAttendance(models.Model):
    servant = models.ForeignKey(Servant)
    date = models.DateField()
    attended_mass = models.BooleanField()
    attended_meeting = models.BooleanField()
    attended_sunday_school = models.BooleanField()
