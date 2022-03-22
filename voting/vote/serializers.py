from rest_framework import serializers
from .models import ResponsibleRepresentative, Blank


class RRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsibleRepresentative
        fields = ('mail','rr_id','password')

class BlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blank
        fields = ('voting_name',
                 'number_of_voters',
                 'number_of_candidates',
                 'date_of_start',
                 'date_of_end',
                 'end_of_elections',
                 'distribution_way')