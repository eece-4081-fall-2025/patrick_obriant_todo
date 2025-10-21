from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskTests(TestCase):
    def test_create_task(self):
        # POST to create
        resp = self.client.post(reverse("task-create"), {
            "title": "Buy milk",
            "notes": "2% gallon",
        })
        self.assertEqual(resp.status_code, 302)  # redirect to list
        self.assertEqual(Task.objects.count(), 1)
        t = Task.objects.first()
        self.assertEqual(t.title, "Buy milk")
        self.assertEqual(t.notes, "2% gallon")
        self.assertFalse(t.completed)

    def test_edit_task(self):
        t = Task.objects.create(title="Orig", notes="n/a")
        resp = self.client.post(reverse("task-update", args=[t.pk]), {
            "title": "Updated",
            "notes": "new notes",
        })
        self.assertEqual(resp.status_code, 302)
        t.refresh_from_db()
        self.assertEqual(t.title, "Updated")
        self.assertEqual(t.notes, "new notes")