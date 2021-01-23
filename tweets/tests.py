from django.test import TestCase

from rest_framework.test import APIClient

from django.contrib.auth import get_user_model
from .models import Tweet

User = get_user_model()

# Create your tests here.
class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='mwaiseghe', password='mypass')
        self.user2 = User.objects.create_user(username='mwaiseghe2', password='mypass2')
        Tweet.objects.create(content="this is a test1", user=self.user)
        Tweet.objects.create(content="this is a test2", user=self.user)
        Tweet.objects.create(content="this is a test3", user=self.user)
        Tweet.objects.create(content="this is a test3", user=self.user2)
        self.currentCount = Tweet.objects.all().count()
        
    def test_user_created(self):
        user = User.objects.get(username="mwaiseghe")
        self.assertEqual(user.username,"mwaiseghe")
        
    def test_tweet_created(self):
        tweet = Tweet.objects.create(content="this is a test2", user=self.user)
        self.assertEqual(tweet.id, 5)
        self.assertEqual(tweet.user, self.user)
        
    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='mypass')
        return client
        
    def test_tweet_list(self):
        client = self.get_client()
        response = client.get("/tweets/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
        print(response.json())
        
    def test_tweets_related_name(self):
        user = self.user
        self.assertEqual(user.tweets.count(), 2)
        
    def test_action_like(self):
        client = self.get_client()
        response = client.post("/tweet/action/", 
                               {"id":2, "action":"like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/tweet/action/", 
                               {"id":2, "action":"unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count,0 )
        user = self.user
        my_like_instances_count = user.tweetlike_set.count()
        self.assertEqual(my_like_instances_count, 0)
        
        
    def test_action_retweet(self):
        client = self.get_client()
        response = client.post("/tweet/action/", 
                               {"id":2, "action":"retweet"})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_id = data.get("id")
        self.assertNotEqual(2, new_id)
        self.assertEqual(self.currentCount +1, new_id)
        
    def test_tweet_create_view(self):
        request_data = {"content":"Test Create View"}
        client = self.get_client()
        response = client.post("/create-tweet/", request_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        new_id = response_data.get("id")
        self.assertEqual(self.currentCount +1, new_id)
        
    def test_tweet_detail_view(self):
        client = self.get_client()
        response = client.get("/tweet/1/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        new_id = data.get("id")
        self.assertEqual(new_id, 1)
        
    def test_delete_view(self):
        client = self.get_client()
        response = client.delete("/tweet/1/delete/")
        self.assertEqual(response.status_code, 200)
        response = client.delete("/tweet/1/delete/")
        self.assertEqual(response.status_code, 404)
        response_incorrect_owner = client.delete("/tweet/4/delete/")
        self.assertEqual(response_incorrect_owner.status_code, 401)