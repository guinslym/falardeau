from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse
import datetime
from django.utils import timezone

class Film(TimeStampedModel):
    name = models.CharField(max_length=12, blank=True, unique=True, null=True)
    screenshot = models.ImageField(upload_to='film/%Y/%m/%d', null=True, blank=True)
    expiring_date = models.DateField(
                            default=(timezone.now() + datetime.timedelta(days=30)),
                            blank=True, null=True,
                            help_text="release date")
    def __str__(self):
        return self.name
    '''
    def get_absolute_url(self):
        return reverse('movies:detail',
                       args=[str(self.id)]
                )
    '''
