from django import forms
from .modelsML import TaskML

class FormML(forms.ModelForm):
    class Meta:
        model = TaskML
        fields = ['email','pclass','sex','age','sibsp','parch','fare','embarked','title']
