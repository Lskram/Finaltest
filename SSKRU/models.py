from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

# หมวดหมู่รายวิชา
class Category(models.Model):
    name = models.CharField(max_length=256) # ชื่อ

    def __str__(self):
        return self.name


# รายวิชา
class Classes(models.Model):
    name = models.CharField(max_length=10) # ชื่อ
    lastname = models.CharField(max_length=256) # นามสกุล
    gender = models.CharField(max_length=256) # เพศ
    age = models.IntegerField() # อายุ
    Educationlevel = models.CharField(max_length=256)
    department = models.ForeignKey(Category, on_delete=models.CASCADE) # หมวดหมู่รายวิชา

    def __str__(self):
        return self.name