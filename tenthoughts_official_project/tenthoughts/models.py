from django.db import models
from django.contrib.auth.models import User


class UserProf(models.Model):
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)

    #Text versions of python lists for storing in the database
    followers = models.TextField(default='email')
    following = models.TextField(default='email')
    groups = models.CharField(max_length=128, default='bschool')


    def followers_list(self):
        followers_list = self.followers.split(',')
        return followers_list

    def following_list(self):
        following_list = self.following.split(',')
        return following_list

    def group_list(self):
        group_list = self.groups.split(',')
        return group_list

    def num_followers(self):
        followers_list = self.followers.split(',')
        return int(len(followers_list)-1)

    def num_following(self):
        following_list = self.following.split(',')
        return int(len(following_list)-1)

    def num_groups(self):
        group_list = self.groups.split(',')
        return len(group_list)

    def __str__(self):
        return self.user.username


class Article(models.Model):
    submitter = models.ForeignKey(UserProf)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    submission_date = models.DateTimeField()


    def __str__(self):
        return self.title

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.TextField(null=True)

    def __str__(self):
        return self.name

class SubmitedArticles(models.Model):
   last_name = models.CharField(max_length=128)
   first_name = models.CharField(max_length=128)
   article_url = models.URLField()
   article_title = models.CharField(max_length=128)
   article2_url = models.URLField(null=True)
   article2_title = models.CharField(max_length=128, null=True)
   article3_url = models.URLField(null=True)
   article3_title = models.CharField(max_length=128, null=True)
   date_submitted = models.DateTimeField(null=True)

   def __unicode__(self):
        return self.last_name

class UserArticles(models.Model):
   client_name = models.CharField(max_length=128)
   client_firstname = models.CharField(max_length=128)
   client_email = models.EmailField()
   title_1 = models.CharField(max_length=128)
   url_1 = models.URLField()
   recommender_1 = models.CharField(max_length=128)
   title_2 = models.CharField(max_length=128)
   url_2 = models.URLField()
   recommender_2 = models.CharField(max_length=128)
   title_3 = models.CharField(max_length=128)
   url_3 = models.URLField()
   recommender_3 = models.CharField(max_length=128)
   title_4 = models.CharField(max_length=128)
   url_4 = models.URLField()
   recommender_4 = models.CharField(max_length=128)
   title_5 = models.CharField(max_length=128)
   url_5 = models.URLField()
   recommender_5 = models.CharField(max_length=128)
   title_6 = models.CharField(max_length=128)
   url_6 = models.URLField()
   recommender_6 = models.CharField(max_length=128)
   title_7 = models.CharField(max_length=128)
   url_7 = models.URLField()
   recommender_7 = models.CharField(max_length=128)
   title_8 = models.CharField(max_length=128)
   url_8 = models.URLField()
   recommender_8 = models.CharField(max_length=128)
   title_9 = models.CharField(max_length=128)
   url_9 = models.URLField()
   recommender_9 = models.CharField(max_length=128)
   title_10 = models.CharField(max_length=128)
   url_10 = models.URLField()
   recommender_10 = models.CharField(max_length=128)

   def __unicode__(self):
        return self.client_firstname
