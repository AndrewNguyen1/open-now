from django.test import TestCase
from django.db import models

from http import HTTPStatus

from .models import *
from django.urls import reverse
from django.urls import resolve

# Create your tests here.

class DummyTestCase(TestCase):
    def setUp(self):
        x = 1
    
    def test_dummy_test_case(self):
        self.assertEqual(1, 1)

class LoginModelTest(TestCase):
    def setUp(self):
        self.login = Login.objects.create(text = 'This is a test')
        self.login.save()
    
    def tearDown(self):
        self.login.delete()

    def test_good_text(self):
        t = 'This is a test'
        self.assertEqual(t, self.login.text)

    def test_bad_text(self):
        t = 'bad text'
        self.assertNotEqual(t, self.login.text)

class BusinessModelTest(TestCase):
    def setUp(self):
        self.business = Business.objects.create(business_name = 'test business', description = 'we sell tests', website = 'www.test.com', phone_number = '1234567890', business_category = 'REST')
        self.business.save()

    def tearDown(self):
        self.business.delete()    

    def test_business(self):
        name = 'test business'
        description = 'we sell tests'
        website = 'www.test.com'
        phone = '1234567890'
        category = 'REST'
        self.assertEqual(name, self.business.business_name)
        self.assertEqual(description, self.business.description)
        self.assertEqual(website, self.business.website)
        self.assertEqual(phone, self.business.phone_number)
        self.assertEqual(category, self.business.business_category)
        name = 'test'
        description = 'we buy tests'
        website = 'www.testing.com'
        phone = '0987654321'
        category = 'SHOP'
        self.assertNotEqual(name, self.business.business_name)
        self.assertNotEqual(description, self.business.description)
        self.assertNotEqual(website, self.business.website)
        self.assertNotEqual(phone, self.business.phone_number)
        self.assertNotEqual(category, self.business.business_category)

class ForumModelTest(TestCase):
    def setUp(self):
        self.forum = Forum.objects.create(name = 'test forum', email = 'test@forum.com', topic = 'topic test', description = 'this is a test', date_created = '01/01/2021')
        self.forum.save()
        
    def tearDown(self):
        self.forum.delete()

    def test_good_forum(self):
        name = 'test forum'
        email = 'test@forum.com'
        topic = 'topic test'
        description = 'this is a test'
        date_created = models.DateTimeField(auto_now_add=True, null=True)
        #year = date_created.year
        self.assertEqual(name, self.forum.name)
        self.assertEqual(email, self.forum.email)
        self.assertEqual(topic, self.forum.topic)
        self.assertEqual(description, self.forum.description)
        #self.assertEqual(year, self.forum.date_created.year)

    def test_bad_forum(self):
        name = ' '
        email = ' '
        topic = ' '
        description = ' '
        date_created = models.DateTimeField(auto_now_add=True, null=True)
        self.assertNotEqual(name, self.forum.name)
        self.assertNotEqual(email, self.forum.email)
        self.assertNotEqual(topic, self.forum.topic)
        self.assertNotEqual(description, self.forum.description)
        self.assertNotEqual(date_created, self.forum.date_created)