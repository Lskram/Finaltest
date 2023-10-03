from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

# หมวดหมู่รายวิชา
class Category(models.Model):
    name = models.CharField(max_length=256) # ชื่อ

    def __str__(self):
        return self.name



class Classes(models.Model):
    name = models.CharField(max_length=10)
    lastname = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    age = models.IntegerField()
    Educationlevel = models.CharField(max_length=256)
    department = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name