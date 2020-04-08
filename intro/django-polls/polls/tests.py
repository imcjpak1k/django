import datetime
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse

from .models import Question
# Create your tests here.

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_plus(self): 
        self.assertEqual(1+2+3, 6) 

    def test_index(self):
        # client create
        client = Client()

        # path : /polls/
        response = client.get(reverse('polls:index'))

        # http 상태값 확인
        self.assertEqual(response.status_code, 200)

        # context에 latest_question_list이 있는지 여부
        self.assertIn('latest_question_list', response.context)
        latest_question_list = response.context['latest_question_list']

        # 객체타입확인
        from django.db.models import QuerySet
        self.assertIsInstance(latest_question_list, QuerySet)

         