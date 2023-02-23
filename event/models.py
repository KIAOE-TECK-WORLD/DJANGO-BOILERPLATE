from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.timezone import make_aware
from django.utils.translation import gettext_lazy as _
from django_countries import Countries
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords

from .enums import (CurrencyType, EventType, SexType,
                    StatusType, TicketType, UserType)
from .managers import UserManager


class G8Countries(Countries):
    only = [
        'BJ', 'BF', 'CI', 'GB', 'ML', 'SN', 'TG',
        ('EU', _('European Union'))
    ]


class BaseDateTime(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, PermissionsMixin, BaseDateTime):
    username   = models.EmailField(max_length=255, unique=True, verbose='My Email Identifier')
    category   = models.CharField(max_length=255, choices=UserType.choices, default=UserType.default())
    email      = models.EmailField(max_length=255, null=True)
    is_active  = models.BooleanField(default=True)
    is_admin   = models.BooleanField(default=False)
    sexType    = models.CharField(max_length=10, choices=StatusType.choices)
    isEnable   = models.BooleanField(default=True)
    identifier = models.CharField(max_length=255, null=True, editable=False)
    verifiedAt = models.DateTimeField(null=True)
    ipAddress  = models.CharField(max_length=255, blank=True, null=True)
    history    = HistoricalRecords()

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'User: {self.username}'

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Event(BaseDateTime):
    name     = models.CharField(max_length=255, unique=True)
    slug     = models.SlugField(max_length=255, unique=True)
    category = models.CharField(max_length=255, choices=EventType.choices)
    isEnable = models.BooleanField(default=True)
    isFree   = models.BooleanField(default=False)
    status   = models.CharField(max_length=30, choices=StatusType.choices, default=StatusType.open())
    cover    = models.ImageField(upload_to='EVENT_COVER')
    code     = models.CharField(max_length=255, editable=False)
    users    = models.ForeignKey(Host, on_delete=models.CASCADE)
    history  = HistoricalRecords()


class EventCalendar(BaseDateTime):
    startDate = models.DateTimeField()
    finalDate = models.DateTimeField()
    country   = CountryField(countries=G8Countries)
    status    = models.CharField(max_length=30, choices=StatusType.choices, default=StatusType.default())
    tags      = models.TextField(null=True)
    location  = models.CharField(max_length=255)
    contacts  = models.CharField(max_length=100)
    condition = models.TextField(null=True)
    places    = models.PositiveIntegerField()
    events    = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventcalendars',)
    history   = HistoricalRecords()


class Ticket(BaseDateTime):
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    currency    = models.CharField(max_length=3, choices=CurrencyType.choices, default=CurrencyType.default())
    cover       = models.ImageField(upload_to='TICKET_COVER', null=True)
    category    = models.CharField(max_length=100, choices=TicketType.choices)
    information = models.JSONField(default=dict)
    identifier  = models.CharField(max_length=255, editable=False)
    calendar    = models.ForeignKey(EventCalendar, on_delete=models.CASCADE, related_name='calendartickets')
    history     = HistoricalRecords()
