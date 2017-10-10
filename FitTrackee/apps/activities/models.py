from django.db import models

import os

from ..user.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Sport(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'sports'
        verbose_name = 'sport'
        verbose_name_plural = 'sports'


class Gpx(models.Model):
    gpx_file = models.FileField(upload_to='gpx/%Y/%m/%d/')

    def filename(self):
        return os.path.basename(self.gpx_file.name)

    def __str__(self):
        return self.filename()

    class Meta:
        db_table = 'gpx'
        verbose_name = 'gpx'
        verbose_name_plural = 'gpx'


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    gpx = models.OneToOneField(Gpx, blank=True, null=True)

    activity_date = models.DateTimeField()
    duration = models.DurationField()
    pauses = models.DurationField(blank=True, null=True)
    moving = models.DurationField(blank=True, null=True)
    distance = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    min_alt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    max_alt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    descent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ascent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    max_speed = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ave_speed = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sport.label + " - " + self.activity_date.strftime('%Y-%m-%d')

    class Meta:
        db_table = 'activities'
        verbose_name = 'activity'
        verbose_name_plural = 'activities'
