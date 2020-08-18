from django.db import models

class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True) # model이 생성된 날짜를 구하려면 auto_now_add를 사용해서 날짜를 구한다.
    updated = models.DateTimeField(auto_now=True) # 새로운 날짜로 업데이트 해야할 경우 auto_now 를 True로 사용한다.

    class Meta:
        abstract = True #DB에 저장되지 않는 코드를 쓸때 abstract를 쓴다.
        