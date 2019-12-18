from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=200)
    teacher=models.CharField(max_length=200)
    count=models.IntegerField(default=0)
    attendence=models.IntegerField(default=0,help_text='0 imply no leniency and 10 imply very lenient',validators=[MaxValueValidator(10),MinValueValidator(0)])
    marks=models.IntegerField(default=0,help_text='0 imply no leniency and 10 imply very lenient',validators=[MaxValueValidator(10),MinValueValidator(0)])
    quality=models.IntegerField(default=0,help_text='0 imply low quality and 10 imply high quality',validators=[MaxValueValidator(10),MinValueValidator(0)])

    def __str__(self):
        return self.name

class Feedback(models.Model):
    course = models.ForeignKey('elective.Course', on_delete=models.CASCADE, related_name='feedback')
    review=models.TextField() 
    name=models.CharField(max_length=200,default='xyz')
    teacher=models.CharField(max_length=200,default='xyz')
    attendence=models.IntegerField(default=0,help_text='0 imply no leniency and 10 imply very lenient',validators=[MaxValueValidator(10),MinValueValidator(0)])
    marks=models.IntegerField(default=0,help_text='0 imply no leniency and 10 imply very lenient',validators=[MaxValueValidator(10),MinValueValidator(0)])
    quality=models.IntegerField(default=0,help_text='0 imply low quality and 10 imply high quality',validators=[MaxValueValidator(10),MinValueValidator(0)])

    def __str__(self):
        return self.review



    