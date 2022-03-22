from email.policy import default
#from operator import mod
#from turtle import numinput
from django.db import models

# Create your models here.

class ResponsibleRepresentative(models.Model):
    mail = models.CharField(null=False, unique=True, max_length=20)
    rr_id = models.CharField(null=False, unique=True, primary_key=True, max_length=20)
    password = models.CharField(null=True, max_length=50)


class Blank(models.Model):
    voting_name = models.CharField(null=False, max_length=20)
    number_of_voters = models.IntegerField(null=False, default=0)
    number_of_candidates = models.IntegerField(null=False,default=0)
    date_of_start = models.DateTimeField(null=False)
    date_of_end = models.DateTimeField(null=False)
    end_of_elections = models.DateTimeField(null=False)
    distribution_way = models.CharField(null=False, max_length=20)


class Voter(models.Model):
    rr_login = models.ForeignKey(Blank, null=False, on_delete=models.CASCADE)
    elections_name = models.CharField(null=False, max_length=20)
    voter_uuid = models.CharField(null=False, unique=True, max_length=20)
