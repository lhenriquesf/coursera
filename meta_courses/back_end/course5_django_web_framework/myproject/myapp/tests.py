from django.test import TestCase
from myapp.models import Booking, Logger
from datetime import datetime
# Create your tests here.

class BookingModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.booking = Booking.objects.create(first_name='Henri',last_name='Souza',guest_count=8,comments='None')

    def test_fields(self):
        self.assertIsInstance(self.booking.first_name, str)
        self.assertIsInstance(self.booking.last_name, str)
        self.assertIsInstance(self.booking.guest_count, int)
        self.assertIsNotNone(self.booking.comments)

    def test_timestamp(self):
        self.assertIsInstance(self.booking.reservation_time, datetime)
