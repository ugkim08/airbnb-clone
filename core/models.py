from django.db import models

class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True #DB에 저장되지 않는 코드를 쓸때 abstract를 쓴다.
        