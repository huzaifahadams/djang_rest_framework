from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    school =models.CharField(max_length=100)
    bio = models.TextField()
    date_enrolled = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return  self.name