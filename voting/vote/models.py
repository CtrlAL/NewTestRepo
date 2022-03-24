from django.db.models import signals
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
#from operator import mod
#from turtle import numinput
from django.db import models
import uuid
# Create your models here.


class ResponsibleRepresentative(models.Model):
    mail = models.CharField(null=False, unique=True, max_length=20)
    rr_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, max_length=20)
    password = models.CharField(null=True, max_length=50)
    is_verified = models.BooleanField(default=False)

def responsiblerepresentative_post_save(sender, instance, signal, *args, **kwards):
    if not instance.is_verified:
        # Send verification email
        send_mail(
            'Verify your RR account',
            'Follow this link to verify your account: '
                'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(instance.rr_id)}),
            settings.DEFAULT_FROM_EMAIL,
            [instance.mail],
            fail_silently=False,
        )
signals.post_save.connect(responsiblerepresentative_post_save, sender=ResponsibleRepresentative)

class Blank(models.Model):
    voting_name = models.CharField(null=False, max_length=20)
    number_of_voters = models.IntegerField(null=False, default=0)
    list_of_candidates = models.JSONField(null=False)
    date_of_start = models.DateTimeField(null=False)
    date_of_end = models.DateTimeField(null=False)
    end_of_elections = models.DateTimeField(null=False)
    distribution_way = models.CharField(null=False, max_length=20)


class Voter(models.Model):
    rr_login = models.ForeignKey(Blank, null=False, on_delete=models.CASCADE)
    elections_name = models.CharField(null=False, max_length=20)
    voter_uuid = models.UUIDField(default=uuid.uuid4,null=False, unique=True, primary_key=True)

class Bulletin(models.Model):
    bulletin_uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    voter = models.OneToOneField(Voter, on_delete=models.CASCADE)
    elections = models.ForeignKey(Blank, on_delete=models.CASCADE)
    downloaded = models.BooleanField(default=False)
    voter_choise = models.CharField(default=None,null=True, max_length=50)


    