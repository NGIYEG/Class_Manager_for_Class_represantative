from django import forms
from django.db import models
from .models import Student, Unit, Enrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'registration_number', 'contact']


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['code', 'name']


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'unit']

# class UnitSelectionForm(forms.Form):
#     student = forms.ModelChoiceField(queryset=Student.objects.all(), label="Select Student")
#     units = forms.ModelMultipleChoiceField(
#         queryset=Unit.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         label="Select Units"
#     )
class StudentRegistrationForm(forms.ModelForm):
    units = forms.ModelMultipleChoiceField(
        queryset=Unit.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Units"
    )

    class Meta:
        model = Student
        fields = ['name', 'registration_number', 'contact']
