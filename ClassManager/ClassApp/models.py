
from django.db import models

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     registration_number = models.CharField(max_length=20, unique=True)
#     contact = models.CharField(max_length=15)
    

#     def __str__(self):
#         return f"{self.name} ({self.registration_number})"

# class Unit(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=10)

#     def __str__(self):
#         return self.name
# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.student.name} - {self.unit.code}"



class Unit(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Student(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    units = models.ManyToManyField(Unit, blank=True)

    def __str__(self):
        return self.name
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.unit.code}"
