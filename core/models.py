from django.db import models

# Create your models here.


class Servant(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.name
    
    
class ServantYear(models.Model):
    servant = models.ForeignKey(Servant)
    year = models.IntegerField()
    sunday_school_class = models.CharField(max_length=255)
    book = models.CharField(max_length=255)


class ServantAttendance(models.Model):
    servant = models.ForeignKey(Servant)
    date = models.DateField()
    attended_mass = models.BooleanField()
    attended_meeting = models.BooleanField()
    attended_sunday_school = models.BooleanField()


class Child(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True)
    father_name = models.CharField(max_length=255, blank=True)
    father_mobile = models.CharField(max_length=255, blank=True)
    father_email = models.EmailField(blank=True)
    mother_name = models.CharField(max_length=255, blank=True)
    mother_mobile = models.CharField(max_length=255, blank=True)
    mother_email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    

class ChildYear(models.Model):
    child = models.ForeignKey(Child)
    year = models.IntegerField()
    sunday_school_class = models.CharField(max_length=255)
    book = models.CharField(max_length=255)
    school_year = models.IntegerField()
