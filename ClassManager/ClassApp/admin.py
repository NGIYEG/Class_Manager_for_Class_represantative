from django.contrib import admin
from .models import Student, Unit, Enrollment

# Register your models here.
admin.site.register(Student)
admin.site.register(Unit)
admin.site.register(Enrollment)
