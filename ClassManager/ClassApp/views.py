from django.shortcuts import render,redirect
from .models import Student, Unit, Enrollment
from .models import Enrollment
from .forms import StudentRegistrationForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})

def unit_list(request):
    units = Unit.objects.all()
    return render(request, "unit_list.html", {"units": units})

def enrollments_summary(request):
    units = Unit.objects.all()
    summary = {unit.name: Enrollment.objects.filter(unit=unit).count() for unit in units}
    return render(request, "enrollments_summary.html", {"summary": summary})
# def unit_selection(request):
#     if request.method == 'POST':
#         form = UnitSelectionForm(request.POST)
#         if form.is_valid():
#             student = form.cleaned_data['student']
#             units = form.cleaned_data['units']

#             # Clear previous enrollments for this student
#             Enrollment.objects.filter(student=student).delete()

#             # Add new enrollments
#             for unit in units:
#                 Enrollment.objects.create(student=student, unit=unit)

#             return redirect('enrollments_summary')  # Redirect to summary or any other page
#     else:
#         form = UnitSelectionForm()

#     return render(request, 'unit_selection.html', {'form': form})
def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            # Save student details
            student = form.save()

            # Save enrollments
            units = form.cleaned_data['units']
            for unit in units:
                Enrollment.objects.create(student=student, unit=unit)

            return redirect('enrollments_summary')  # Redirect to summary or another page
    else:
        form = StudentRegistrationForm()

    return render(request, 'student_register.html', {'form': form})