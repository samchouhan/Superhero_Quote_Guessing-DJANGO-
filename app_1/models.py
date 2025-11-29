from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    enrollment_number = models.CharField(max_length=50, unique=True) 
    dateof_birth = models.DateField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"(self.name) - {self.enrollment_number}"   