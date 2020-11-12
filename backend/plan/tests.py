from django.test import TestCase,Client
from django.core.files import File
from .models import Plan
from django.contrib.auth.models import User
from location.models import Location


import json

class PlanTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='test_id', password='test_pw')
        Location.objects.create(name='loc_name_1', latitude = -11.1111111, longitude = 22.2222222)
        #Plan.objects.create(author=User.objects.first(), destination=Location.objects.first(), duration = '20201111-20201113', keywords = 'beach', like_cnt = 3, gallery_thumbnail = 'test_image.jpg')

    def test_model(self):
        '''
        plan = Plan()
        plan.author = User.objects.get(id=1)
        plan.destination = Location.objects.get(id=1)
        plan.dutation = '3'
        plan.keywords = 'honeymoon'
        plan.like_cnt = 5
        plan.gallery_thumbnail = File(open("test_image.jpg", encoding='utf-16'))
        plan.save()
        '''

        Plan.objects.create(author=User.objects.first(), destination=Location.objects.first(), duration = '20201111-20201113', keywords = 'beach', like_cnt = 3, gallery_thumbnail = File(open('test_image.jpg', encoding = 'utf-16')))

        p = Plan.objects.get(id=1).gallery_thumbnail.path
        
        self.failUnless(open(p), 'file not found')

    '''
    def test_get_plan_id(self):
        client = Client()
        response = client.get('/api/plan/1/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('beach', response.content.decode()) 
    '''
# Create your tests here.
