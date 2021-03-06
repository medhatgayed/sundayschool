import uuid
from django.db import models
from datetime import datetime, date

# Create your models here.


class SundaySchoolClass(models.Model):
    name = models.CharField(max_length=255, blank=True)
    book = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name
    
    def get_servants_emails(self):
        return [servant.email for servant in self.servant_set.all() if servant.email]

    def get_active_servants(self):
        return self.servant_set.filter(is_active=True)

    def get_active_children(self):
        return self.child_set.filter(is_active=True)
        
        
class Servant(models.Model):
    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    sunday_school_class = models.ForeignKey(SundaySchoolClass, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name

    def get_first_name(self):
        return self.name.split()[0].title()

class ServantAttendance(models.Model):
    servant = models.ForeignKey(Servant)
    date = models.DateField()
    attended_mass = models.BooleanField()
    attended_meeting = models.BooleanField()
    attended_sunday_school = models.BooleanField()


class ChildParents(models.Model):
    phone = models.CharField(max_length=255, blank=True)
    father_name = models.CharField(max_length=255, blank=True)
    father_mobile = models.CharField(max_length=255, blank=True)
    father_email = models.EmailField(blank=True)
    mother_name = models.CharField(max_length=255, blank=True)
    mother_mobile = models.CharField(max_length=255, blank=True)
    mother_email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    
    def __unicode__(self):
        return self.get_parents_names()
    
    def get_parents_names(self):
        parents_names = ''
        
        if self.father_name:
            parents_names += self.father_name.split()[0].title()
            
        if self.mother_name:
            if parents_names:
                parents_names += ' and '
            parents_names += self.mother_name.split()[0].title()
    
        return parents_names or 'Parents'
    
    def get_parents_emails(self):
        parents_emails = []
        
        if self.father_email:
            parents_emails.append(self.father_email)
            
        if self.mother_email and (self.father_email != self.mother_email):
            parents_emails.append(self.mother_email)
            
        return parents_emails


class Child(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    school_year = models.IntegerField(null=True, blank=True)
    child_parents = models.ForeignKey(ChildParents, null=True, blank=True)
    sunday_school_class = models.ForeignKey(SundaySchoolClass, null=True, blank=True)
    sent_emails = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    
    def __unicode__(self):
        return self.name
    
    def get_first_name(self):
        return self.name.split()[0].title()

    def parse_and_set_dob(self, dob_str):
        for dob_format in ('%Y-%m-%d', '%d/%m/%Y'):
            try:
                dobdt = datetime.strptime(dob_str, dob_format)
            except ValueError:
                pass
            else:
                self.dob = date(year=dobdt.year, month=dobdt.month, day=dobdt.day)