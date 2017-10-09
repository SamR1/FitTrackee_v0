from django.db import models

from ..user.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Sport(models.Model):
    label = models.CharField(max_length=50)

    class Meta:
        db_table = 'sports'


class Gpx(models.Model):
    gpx_file = models.FileField(upload_to=user_directory_path)

    class Meta:
        db_table = 'gpx'


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    gpx = models.OneToOneField(Gpx)

    activity_date = models.DateField()
    duration = models.DurationField()
    pauses = models.DurationField()
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    min_alt = models.DecimalField(max_digits=5, decimal_places=2)
    max_alt = models.DecimalField(max_digits=5, decimal_places=2)
    descent = models.DecimalField(max_digits=5, decimal_places=2)
    ascent = models.DecimalField(max_digits=5, decimal_places=2)
    max_speed = models.DecimalField(max_digits=5, decimal_places=2)
    ave_speed = models.DecimalField(max_digits=5, decimal_places=2)

    creation_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'activities'
