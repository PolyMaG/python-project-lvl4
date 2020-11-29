from django.test import TestCase

from tasks.forms import TagForm, TaskForm


class TagFormTest(TestCase):
    def test_tag_form_title_field_label(self):
        form = TagForm()
        self.assertTrue(
            form.fields["title"].label is None or form.fields["title"].label == "Title"
        )

    def test_tag_form(self):
        form_data = {"title": "test title"}
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())


class TaskFormTest(TestCase):
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


"""
    def test_task_form(self):
        form_data = {
            "name": "test name",
            "description": "test descrition",
            # "status": "test status",
            # "assigned_to": "test assigned",
            # "tags": "test tag",
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
"""
