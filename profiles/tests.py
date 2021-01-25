from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

# Create your tests here.
User = get_user_model()

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='mwaiseghe', password='mypass')
        self.user2 = User.objects.create_user(username='mwaiseghe2', password='mypass2')
        
    def test_profile_created(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(),2)
        
    def test_following(self):
        user1 = self.user
        user2 = self.user2      
        user1.profile.followers.add(user2)
        qs = user2.following.filter(user=user1)
        self.assertTrue(qs.exists())
        user1_following = user1.following.all()
        self.assertFalse(user1_following.exists())
        