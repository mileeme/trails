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

# class Category(models.Model):
#     class Meta:
#         verbose_name_plural = 'categories'
#     name = models.CharField('category', max_length=50)
#     def __str__(self):
#         return f"{self.name}"
#
#
# class SubCategory(models.Model):
#     class Meta:
#         verbose_name_plural = 'subcategories'
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField('sub-category', max_length=50)
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Organizer(models.Model):
#     name = models.CharField('organizer', max_length=255)
#     web = models.URLField(max_length=255, blank=True)
#     email = models.EmailField('email address')
#     area_code = models.CharField('area code', blank=True, max_length=5)
#     phone = models.CharField('phone number', blank=True, max_length=10)
#     photo = models.ImageField(default='example.jpg', upload_to='organizer_photo', blank=True)
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Venue(models.Model):
#     name = models.CharField('venue name', max_length=255)
#     address = models.CharField('venue address', max_length=255)
#     city = models.CharField('venue city', max_length=50)
#     state = models.CharField('venue state', max_length=255)
#     zip = models.CharField('venue zip code', max_length=20)
#     def __str__(self):
#         return f"{self.name} {self.city}, {self.state} {self.zip}"
#
#
# class Distance(models.Model):
#     length = models.DecimalField(max_digits=4, decimal_places=1)
#     kilometers = 'km'
#     miles = 'mi'
#     DISTANCE_TYPE_CHOICES = [
#         (kilometers, 'km'),
#         (miles, 'mi')
#     ]
#     distance_type = models.CharField(
#         max_length=5,
#         choices=DISTANCE_TYPE_CHOICES,
#         default=miles,
#     )
#     def __str__(self):
#         return f"{self.length}{self.distance_type}"
#
#
# class Event(models.Model):
#     subcategory = models.ManyToManyField(SubCategory, through='SubCatEventM2M')
#     distance = models.ManyToManyField(Distance, through='EventDistanceM2M')
#     organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
#     venue = models.ForeignKey(Venue, on_delete=models.PROTECT)
#     title = models.CharField('event title', max_length=255)
#     start = models.DateField('start date')
#     end = models.DateField('end date')
#     photo = models.ImageField(default='event_photo/IMG_4149.jpg', upload_to='event_photo', blank=True)
#     capacity = models.IntegerField('capacity', blank=True, null=True)
#     description = models.CharField(max_length=2000)
#     def __str__(self):
#         return f"{self.title}"
#
#
# # m2m for subcategory and events
# class SubCatEventM2M(models.Model):
#     subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.event} {self.subcategory}"
#
#
# # m2m for distance and events
# class EventDistanceM2M(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.PROTECT)
#     distance = models.ForeignKey(Distance, on_delete=models.PROTECT)
#     def __str__(self):
#         return f"{self.event} {self.distance}"
#
#
# class DistanceDetail(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     distance = models.ForeignKey(Distance, on_delete=models.CASCADE)
#     start_time = models.DateTimeField('start time')
#     cutoff_time = models.DateTimeField('cuttoff time')
#     total_capacity = models.IntegerField('capacity', blank=True, null=True)
#     def __str__(self):
#         return f"{self.event} {self.distance} {self.total_capacity}"
#
#
# class Registration(models.Model):
#     distance_detail = models.ForeignKey(DistanceDetail, on_delete=models.CASCADE)
#     date = models.DateField('registration date')
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     def __str__(self):
#         return f"{self.distance_detail} {self.date} {self.price}"

# class Participant(models.Model):
#     first_name = models.CharField('first name', max_length=255)
#     last_name = models.CharField('last name', max_length=255)
#     female = 'female'
#     male = 'male'
#     other = 'other'
#     GENDER_CHOICES = [
#         (female, 'F'),
#         (male, 'M'),
#         (other, 'other'),
#     ]
#     gender = models.CharField(
#         max_length=10,
#         choices=GENDER_CHOICES,
#         default=female,
#         blank=True,
#     )
#     birthdate = models.DateTimeField('date of birth')
#     email = models.EmailField('email address')
#     area_code = models.CharField('area code', max_length=5, blank=True)
#     phone = models.CharField('phone', max_length=10, blank=True)
#     emergency_contact_name = models.CharField('emergency contact name', max_length=50)
#     emergency_contact_area_code = models.CharField('emergency contact area code', max_length=5)
#     emergency_contact_phone = models.CharField('emergency contact phone', max_length=10)
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} - {self.gender} {self.email}"
