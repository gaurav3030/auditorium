from django.db import models

# Create your models here.
class booking(models.Model):
    venue= models.CharField(max_length=100);
    event_name = models.CharField(max_length=100);
    date = models.DateField();
    
    email = models.EmailField();
    FILTER_CHOICES = (
        ('First Half', 'First Half'),
        ('Second Half', 'Second Half'),
        ('Full Day', 'Full Day'),
    )
    FILTER = (
        ('VES College of Architecture','VES College of Architecture'),
        ('VES Institute of Technology','VES Institute of Technology'),
        ('VES College of Pharmacy','VES College of Pharmacy'),
        ('VES College of Law','VES College of Law'),
        ('VES Institute of Management','VES Institute of Management'),
    )

    time = models.CharField(max_length=100,choices = FILTER_CHOICES)
    college = models.CharField(max_length=100,choices = FILTER)
    FILTER_APPROVE = (
        ('Not Approved', 'Not Approved'),
        ('Approved', 'Approved'),
        
    )
    approve= models.CharField(max_length=100,choices = FILTER_APPROVE,default='Not Approved')