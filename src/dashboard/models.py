from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    class_level = models.IntegerField()
    subjects = models.CharField(max_length=255)  # Assuming a comma-separated string for simplicity
    gender = models.CharField(max_length=10)
    
    # Father details
    father_first_name = models.CharField(max_length=100)
    father_last_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)

    # Mother details
    mother_first_name = models.CharField(max_length=100)
    mother_last_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)