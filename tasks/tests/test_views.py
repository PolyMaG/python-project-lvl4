from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from tasks.forms import TaskFilter
from tasks.models import Tag, Task, TaskStatus


class TaskListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Run once for every test method to setup clean data.
        User.objects.create_user(
            username="test1", password="12test12", email="test@example.com"
        )
        TaskStatus.objects.create(name="test")
        user = User.objects.get(id=1)
        status = TaskStatus.objects.get(id=1)
        Task.objects.create(
            name="TestTask",
            description="description",
            status=status,
            creator=user,
            assigned_to=user,
        )

    def setUp(self):
        # Run once for every test method to setup clean data.
        self.client.login(username="test1", password="12test12")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get("/task-manager/tasks/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse("tasks:tasks_list_url"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("tasks:tasks_list_url"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "tasks/tasks_list.html")

    def test_lists_all_tasks(self):
        f = TaskFilter(queryset=Task.objects.all())
        resp = self.client.get(reverse("tasks:tasks_list_url"))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(f.qs) == 1)


class TagListViewTest(TestCase):
    def setUp(self):
        # Run once for every test method to setup clean data.
        test_user1 = User.objects.create_user(
            username="test1", password="12test12", email="test@example.com"
        )
        test_user1.save()
        self.client.login(username="test1", password="12test12")

    @classmethod
    def setUpTestData(cls):
        # Run once for every test method to setup clean data.
        Tag.objects.create(title="test tag")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get("/task-manager/tags/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse("tasks:tags_list_url"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("tasks:tags_list_url"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "tasks/tags_list.html")

    def test_lists_all_tags(self):
        resp = self.client.get(reverse("tasks:tags_list_url"))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context["tags"]) == 1)


class StatusListViewTest(TestCase):
    def setUp(self):
        # Run once for every test method to setup clean data.
        test_user1 = User.objects.create_user(
            username="test1", password="12test12", email="test@example.com"
        )
        test_user1.save()
        self.client.login(username="test1", password="12test12")

    @classmethod
    def setUpTestData(cls):
        # Run once for every test method to setup clean data.
        TaskStatus.objects.create(name="test")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get("/task-manager/statuses/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse("tasks:status_list_url"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("tasks:status_list_url"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "tasks/status_list.html")

    def test_lists_all_tags(self):
        resp = self.client.get(reverse("tasks:status_list_url"))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context["status_all"]) == 1)


class MyTasksListViewTest(TestCase):
    def setUp(self):
        # Run once for every test method to setup clean data.
        test_user1 = User.objects.create_user(
            username="test1", password="12test12", email="test@example.com"
        )
        test_user1.save()
        test_user2 = User.objects.create_user(
            username="test2", password="12test12", email="test@example.com"
        )
        test_user2.save()
        test_status = TaskStatus.objects.create(name="test")
        test_status.save()
        test_task1 = Task(
            name="TestTask1",
            description="description",
            status=test_status,
            creator=test_user1,
            assigned_to=test_user2,
        )
        test_task1.save()
        test_task2 = Task(
            name="TestTask2",
            description="description",
            status=test_status,
            creator=test_user1,
            assigned_to=test_user2,
        )
        test_task2.save()
        test_task3 = Task(
            name="TestTask3",
            description="description",
            status=test_status,
            creator=test_user2,
            assigned_to=test_user1,
        )
        test_task3.save()

    def test_logged_in_uses_correct_template(self):
        self.client.login(username="test1", password="12test12")
        resp = self.client.get(reverse("index_url"))

        # log in user
        self.assertEqual(str(resp.context["user"]), "test1")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "index.html")

    def test_only_my_tasks_in_list(self):
        # test that three tasks were created
        self.client.login(username="test1", password="12test12")
        f = TaskFilter(queryset=Task.objects.all())
        resp_all = self.client.get(reverse("tasks:tasks_list_url"))
        self.assertEqual(resp_all.status_code, 200)
        self.assertEqual(len(f.qs), 3)

        # log in user1
        self.client.login(username="test1", password="12test12")
        resp = self.client.get(reverse("tasks:tasks_list_url"))
        self.assertEqual(str(resp.context["user"]), "test1")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue("filter" in resp.context)

        # test that only two tasks were created by user1
        f = TaskFilter(queryset=Task.objects.filter(creator=resp.context["user"]))
        self.assertEqual(len(f.qs), 2)

        # test that all tasks in 'my list' were created by user1
        f = TaskFilter(queryset=Task.objects.filter(creator=resp.context["user"]))
        for task in f.qs:
            self.assertEqual(resp.context["user"], task.creator)


class AssignedToListViewTest(TestCase):
    def setUp(self):
        # Run once for every test method to setup clean data.
        test_user1 = User.objects.create_user(
            username="test1", password="12test12", email="test@example.com"
        )
        test_user1.save()
        test_user2 = User.objects.create_user(
            username="test2", password="12test12", email="test@example.com"
        )
        test_user2.save()

    def test_all_users_in_list(self):
        # test that two users were created
        resp_all = self.client.get(reverse("tasks:users_list_url"))
        self.assertEqual(resp_all.status_code, 200)
        self.assertEqual(len(resp_all.context["users"]), 2)
