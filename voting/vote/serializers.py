from rest_framework import serializers
from .models import ResponsibleRepresentative, Blank , Voter, Bulletin


class RRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsibleRepresentative
        fields = ('mail','rr_id','password', 'is_verified')

class BlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blank
        fields = ('voting_name',
                 'number_of_voters',
                 'list_of_candidates',
                 'date_of_start',
                 'date_of_end',
                 'end_of_elections',
                 'distribution_way')

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ('rr_login','elections_name','voter_uuid')

class BulletinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bulletin
        fields = ('bulletin_uuid','voter_choise', 'voter')