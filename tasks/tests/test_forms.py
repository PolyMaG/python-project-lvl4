from django.contrib.auth.models import User
from django.test import TestCase

from tasks.forms import TagForm, TaskForm
from tasks.models import TaskStatus


class TagFormTest(TestCase):
    def test_tag_form(self):
        form_data = {"title": "test title"}
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_tag_form_title_field_label(self):
        form = TagForm()
        self.assertTrue(
            form.fields["title"].label is None or form.fields["title"].label == "Title"
        )


class TaskFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified data for all class methods.
        User.objects.create_user(
            username="test1", password="12test12", email="test@example.com"
        )
        TaskStatus.objects.create(name="test")

    def test_task_form(self):
        user = User.objects.get(id=1)
        status = TaskStatus.objects.get(id=1)
        form_data = {
            "name": "test name",
            "description": "test descrition",
            "status": status,
            "assigned_to": user,
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_name_field_label(self):
        form = TaskForm()
        self.assertTrue(
            form.fields["name"].label is None or form.fields["name"].label == "Name"
        )

    def test_task_form_description_field_label(self):
        form = TaskForm()
        self.assertTrue(
            form.fields["description"].label is None
            or form.fields["description"].label == "Description"
        )

    def test_task_form_status_field_label(self):
        form = TaskForm()
        self.assertTrue(
            form.fields["status"].label is None
            or form.fields["status"].label == "Status"
        )

    def test_task_form_assigned_field_label(self):
        form = TaskForm()
        self.assertTrue(
            form.fields["assigned_to"].label is None
            or form.fields["assigned_to"].label == "Assigned to"
        )

    def test_task_form_tags_field_label(self):
        form = TaskForm()
        self.assertTrue(
            form.fields["tags"].label is None or form.fields["tags"].label == "Tags"
        )
