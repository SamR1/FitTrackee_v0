from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Count


def get_image_path(instance, filename):
    return 'pictures/user_{0}/{1}'.format(instance.id, filename)


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    follows = models.ManyToManyField("self", related_name='followed_users', blank=True,
                                     symmetrical=False)

    def get_activities_count(self):
        user = User.objects.filter(pk=self.id).annotate(activity__count=Count('activity'))
        return user[0].activity__count

    def get_friends(self):
        friends = self.follows.all()
        # only friends who accepted friend requests
        friends_list = [friend.id for friend in friends if self in friend.follows.all()]
        return friends_list
