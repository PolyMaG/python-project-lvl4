import django_filters
from django import forms

from .models import Tag, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "assigned_to", "tags"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "assigned_to": forms.Select(attrs={"class": "form-control"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-control"}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["title"]

        widgets = {"title": forms.TextInput(attrs={"class": "form-control"})}


class TaskFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")
    creator = django_filters.BooleanFilter()

    class Meta:
        model = Task
        fields = ["status", "assigned_to", "tags"]
