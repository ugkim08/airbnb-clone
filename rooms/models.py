from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

class AbstractItem(core_models.TimeStampedModel):

    """ AbstractItem """
    
    name = models.CharField(max_length=80)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class RoomType(AbstractItem):

    class Meta:
        verbose_name = "Room Type"

class Amenity(AbstractItem):

    """Amenity RoomType Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"

class Facility(AbstractItem):

    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"

class HouseRule (AbstractItem):

    """House Rule Definition"""

    class Meta:
        verbose_name = "House Rule"

class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    adress = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE) # on delete : forignkey로 연결된 User를 삭제할 경우 해당 User와 연결된 Room도 함께 삭제된다는 의미이다. CASCADE = 폭포수 효과.
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenites = models.ManyToManyField("Amenity", blank=True)
    facilites = models.ManyToManyField("Facility", blank=True)
    house_rule = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
