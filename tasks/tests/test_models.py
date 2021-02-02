from django.contrib.auth.models import User
from django.test import TestCase

from tasks.models import Tag, Task, TaskStatus


class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified data for all class methods.
        Tag.objects.create(title="New tag")

    def test_title_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field("title").verbose_name
        self.assertEquals(field_label, "title")

    def test_title_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field("title").max_length
        self.assertEquals(max_length, 50)

    def test_tag_name(self):
        tag = Tag.objects.get(id=1)
        tag_name = tag.title
        self.assertEquals(tag_name, str(tag))


class StatusModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified data for all class methods.
        TaskStatus.objects.create(name="test")

    def test_status_label(self):
        status = TaskStatus.objects.get(id=1)
        field_label = status._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_status_max_length(self):
        status = TaskStatus.objects.get(id=1)
        max_length = status._meta.get_field("name").max_length
        self.assertEquals(max_length, 4)

    def test_status_name(self):
        status = TaskStatus.objects.get(id=1)
        status_name = status.name
        self.assertEquals(status_name, str(status))


class TaskModelTest(TestCase):
    def setUp(self):
        # Run once for every test method to setup clean data.
        self.user1 = User.objects.create_user(
            username="test1", password="12test12", email="test@example.com"
        )
        self.user2 = User.objects.create_user(
            username="test2", password="12test12", email="test@example.com"
        )
        self.user1.save()
        self.user2.save()
        self.status = TaskStatus.objects.create(name="test")
        self.status.save()
        self.task = Task(
            name="TestTask",
            description="description",
            status=self.status,
            creator=self.user1,
            assigned_to=self.user2,
        )
        self.task.save()

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()

    def test_name_max_length(self):
        max_length = self.task._meta.get_field("name").max_length
        self.assertEquals(max_length, 200)

    def test_task_name(self):
        self.assertEquals(self.task.name, str(self.task))

    def test_absolute_url(self):
        self.assertEquals(self.task.get_absolute_url(), "/tasks/task/1/")

    def test_read_task(self):
        self.assertEqual(self.task.status, self.status)
        self.assertEqual(self.task.creator, self.user1)
        self.assertEqual(self.task.assigned_to, self.user2)
        self.assertEqual(self.task.description, "description")

    def test_update_task_(self):
        self.task.description = "new description"
        self.task.assigned_to = self.user1
        self.task.save()
        self.assertEqual(self.task.description, "new description")
        self.assertEqual(self.task.assigned_to, self.user1)
