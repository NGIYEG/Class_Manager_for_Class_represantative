"""
Class Rep Class Manager

Overview

The Class Rep Class Manager is a web application designed to streamline the management of class members' data for class representatives or administrators. Built with Django, it offers functionalities to view, update, and manage student details, including names, registration numbers, contact information, and registered units for the current semester.

Project Structure

The project is organized using a typical Django directory structure:

ClassManager/: Contains the core Django project files like settings.py, urls.py, and wsgi.py.

ClassApp/: This directory houses your Django app, which includes models, views, forms, templates, and static files.

models.py: Defines the data models representing students, units (courses), and enrollments.
views.py: Contains functions that handle user requests and interactions with the database.
forms.py: Includes form classes for creating and managing students, units, and enrollments.
templates/: Holds HTML templates for rendering the application's user interface.
static/: Stores static files such as CSS stylesheets, JavaScript code, and images.
manage.py: A utility script for managing the Django project (running migrations, creating a superuser, etc.).

requirements.txt: Lists the required Python packages for the project.

Models

The project utilizes three main models defined in models.py:

Student: Represents a student in the class and stores their name, registration number, contact information, and the units they are enrolled in (many-to-many relationship).
Unit: Represents a unit/course offered in the semester, including its name and code.
Enrollment: Links a student to a specific unit, indicating their enrollment in that course.

Forms

The application utilizes forms defined in forms.py to handle user input for creating and updating data:

StudentForm: Used for creating and editing student information.
UnitForm: Used for creating and editing unit information.
EnrollmentForm: Used for enrolling students in specific units.
StudentRegistrationForm: A comprehensive form for registering a new student and selecting the units they are enrolling in.

Views

The views in views.py handle the application's logic and interact with the models and forms to process user requests. They also render the appropriate templates:
Home View: Displays the application's homepage with general information.
Student List View: Displays a list of all registered students.
Student Registration View: Handles registering a new student and their unit selections.
Enrollment Summary View: Provides a summary of student enrollments for each unit.
Templates

The application relies on HTML templates located in the templates directory to deliver the user interface. These templates display data retrieved from the models and incorporate forms for user interaction.

Static Files

Static files (CSS, JavaScript, and images) are stored in the static directory and add styling, interactivity, and visual elements to the application:

CSS (style.css,style2.css): Defines styles for the application's layout and visual appearance.
JavaScript (script.js): Includes code for dynamic behavior and user interactions(EventListeners).
Images (background.jpg): An image used as the background for the homepage.


**Conclusion**

The Class Rep Class Manager provides a user-friendly web application for managing class data. It leverages Django's capabilities to offer a well-structured and efficient solution for class representatives or administrators.

"""