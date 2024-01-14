from django import forms
from course_management.models import ShortTermCourse

class LoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True)


class ShortTermCourseForm(forms.Form):
    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=2000)
    description = forms.CharField(max_length=20000)
    image = forms.ImageField(required=False)
    amount = forms.FloatField()
    additional_information = forms.CharField(max_length=20000)
    status = forms.CharField(max_length=10)