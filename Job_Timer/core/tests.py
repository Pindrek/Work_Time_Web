from django.test import TestCase
from django.urls import reverse
import json
from .models import WorkSession
from datetime import timedelta
from django.utils import timezone

# Create your tests here.

class HomeTest(TestCase):

    def test_home_wrong_request_method(self):
        response = self.client.put(reverse('home'))
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json()["method"], False)

    def test_home_add_choice(self):
        response = self.client.post(reverse('home'),
        data=json.dumps({"progress_bar": 20, "progress": "P0DT03H41M12S"}),
        content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["create"
        ], True)
        self.assertEqual(WorkSession.objects.count(), 1)
        session = WorkSession.objects.first()
        self.assertEqual(session.progress, timedelta(hours=3, minutes=41, seconds=12))

    def test_home_add_choice_exists(self):
        first_add = self.client.post(reverse('home'),
        data=json.dumps({"progress_bar": 0, "progress": "P0DT00H00M00S"}),
        content_type="application/json")
        self.assertEqual(first_add.status_code, 200)
        self.assertEqual(first_add.json()["create"], True)
        second_add = self.client.post(reverse('home'),
        data=json.dumps({"progress_bar": 0, "progress": "P0DT00H00M00S"}),
        content_type="application/json")
        self.assertEqual(second_add.status_code, 409)
        self.assertEqual(second_add.json()["create"], "exists")

    def test_home_update_choice(self):
        add = self.client.post(reverse('home'),
        data=json.dumps({"progress_bar": 20, "progress": "P0DT03H41M12S"}),
        content_type="application/json")
        self.assertEqual(add.status_code, 200)
        self.assertEqual(add.json()["create"], True)
        self.assertEqual(WorkSession.objects.count(), 1)
        response = self.client.patch(reverse('home'),
        data=json.dumps({"progress_bar": 75, "progress": "P0DT09H33M33S"}),
        content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["update"], True)
        session = WorkSession.objects.first()
        self.assertEqual(session.progress_bar, 75)
        self.assertEqual(session.progress, timedelta(hours=9, minutes=33, seconds=33))

    def test_home_view_choice(self):
        WorkSession.objects.create(progress_bar = 20,
                                   progress = timedelta(hours=1, minutes=30, seconds=45),
                                   date = timezone.localdate())
        response = self.client.get(reverse('home'))
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data[0]["id"], 1)
        self.assertEqual(data[0]["progress_bar"], 20)
        self.assertEqual(data[0]["progress"], "P0DT01H30M45S")
        self.assertEqual(data[0]["date"], str(timezone.localdate()))