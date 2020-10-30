from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    father_name=models.CharField(max_length=30)
    mob=models.IntegerField()
    add=models.CharField(max_length=100)
    course_name=models.ForeignKey('course', on_delete=models.CASCADE, default=1)

    class Meta:
        db_table='student'

    def __str__(self):
        return self.name
    
class trainer(models.Model):
    name=models.CharField(max_length=30)
    sub=models.CharField(max_length=30)
    desc=models.CharField(max_length=100)
    salary=models.FloatField()
    trainer_image=models.ImageField(upload_to="img/trainers", default="")

    def __str__(self):
        return self.name

class course(models.Model):
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=30, default=1)
    course_desc=models.CharField(max_length=1000, default="")
    trainer_name=models.ForeignKey('trainer', on_delete=models.CASCADE, default=1)
    duration=models.IntegerField()
    fee=models.FloatField()
    seat=models.IntegerField()
    courses_image=models.ImageField(upload_to="img/courses", default="")

    def __str__(self):
        return self.name
