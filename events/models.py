from django.db import models
from django import forms


# distance
class Distance(models.Model):
    # length = models.DecimalField(max_digits=4, decimal_places=1)
    length = models.PositiveIntegerField('distance')
    kilometers = 'km'
    miles = 'mi'
    DISTANCE_TYPE_CHOICES = [
        (kilometers, 'km'),
        (miles, 'mi')
    ]
    distance_type = models.CharField(
        max_length=5,
        choices=DISTANCE_TYPE_CHOICES,
        default=miles,
        blank=True,
    )
    def __str__(self):
        return f"{self.length} {self.distance_type}"

# organizer
class Organizer(models.Model):
    name = models.CharField('organizer', max_length=255)
    web = models.URLField('web', max_length=255, blank=True, null=True)
    def __str__(self):
        return f"{self.name}"

# SubCategory
class SubCategory(models.Model):
    name = models.CharField('sub category', max_length=50)
    class Meta:
        verbose_name_plural = 'subcategories'
    def __str__(self):
        return f"{self.name}"

class Event(models.Model):
    # distance = models.ManyToManyField(Distance)
    distance = models.ManyToManyField(Distance, through='EventDistanceM2M')
    subcategory = models.ManyToManyField(SubCategory, through='SubCatEventM2M')
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    title = models.CharField('event title', max_length=255)
    # photo = models.ImageField(default='event_photo/trail-running-essentials.jpg', upload_to='event_photo', blank=True, null=True)
    register = models.URLField('registeration link', max_length=255)
    date = models.DateField('start date')
    city = models.CharField('city', max_length=50)
    state = models.CharField('state', max_length=3)
    zip = models.CharField('zip code', max_length=20)
    # web = models.URLField('organizer link', max_length=255, blank=True, null=True)
    detail = models.CharField(max_length=2000, blank=True, null=True)
    def __str__(self):
        return f"{self.title} {self.date} {self.city} {self.state}"

# photos (Event to many photos)
class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    photo = models.URLField('photo link', max_length=255, blank=True, null=True)
    def __str__(self):
        return f"{self.photo}"

# EventDistance M2M
class EventDistanceM2M(models.Model):
    distance = models.ForeignKey(Distance, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.distance} {self.event}"

# EventSubCategory M2M
class SubCatEventM2M(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.event} {self.subcategory}"
