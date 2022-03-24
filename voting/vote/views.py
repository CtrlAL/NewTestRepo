from vote.serializers import RRSerializer, BlankSerializer , BulletinSerializer, VoterSerializer
import uuid
from rest_framework import status
from .models import Blank, ResponsibleRepresentative, Bulletin, Voter
from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import string
import secrets

# Create your views here.

class ResponsibleRepresentativeViev(APIView):
    def get(self, request):
        rrs = ResponsibleRepresentative.objects.all()
        serializer = RRSerializer(rrs, many=True)
        return Response(serializer.data)

    def post(self, request):
        mail = request.data['mail']
        #send_mail("someting", "somethingmassage",from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=["sasha.lartsev@gmail.com"],fail_silently=False)
        #rr_id = uuid.uuid4()
        #print(rr_id)
        rr = ResponsibleRepresentative(mail)
        rr.save()
        serializer = RRSerializer(rr)
        return Response(serializer.data)

    def put(self, request):
        rr = ResponsibleRepresentative.objects.get(pk=request.data['uuid'])
        alphabet = string.ascii_letters + string.digits 
        rr.password = ''.join(secrets.choice(alphabet) for i in range(8))
        rr.save()
        serializer = RRSerializer(rr)
        return Response(serializer.data)

    def delete(self,request):
        try:
            ResponsibleRepresentative.objects.all().delete()
        except ResponsibleRepresentative.DoesNotExist:
            return Response("Does not exist")

        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def verify(request, uuid):
    try:
        rr = ResponsibleRepresentative.objects.get(rr_id=uuid, is_verified=False)
    except ResponsibleRepresentative.DoesNotExist:
       return Response("RR already verified", status=status.HTTP_204_NO_CONTENT)

    rr.is_verified = True
    alphabet = string.ascii_letters + string.digits
    rr.password = ''.join(secrets.choice(alphabet) for i in range(8))
    rr.save()
    serializer = RRSerializer(rr)
    return Response(serializer.data)


class BlankViev(APIView):
    def get(self, request):
        blank = Blank.objects.all()
        serializer = BlankSerializer(blank, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = BlankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


    def delete(self, request):
        try:
            Blank.objects.all().delete()
        except Blank.DoesNotExist:
            return Response("Does not exist")

        return Response(status=status.HTTP_204_NO_CONTENT)
    


class VoterViev(APIView):
    def get(self, request):
        blank = Voter.objects.all()
        serializer = VoterSerializer(blank, many=True)
        return Response(serializer.data)


    def post(self, request):
        try:
            blank = Blank.objects.get(voting_name=request.data["elections_name"])
            voter = blank.voter_set.create()
            voter.elections_name = request.data["elections_name"]
            voter.save()
            serializer = VoterSerializer(voter)
        except Blank.DoesNotExist:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        return Response(serializer.data)


    def delete(self, request):
        try:
            Voter.objects.all().delete()
        except Voter.DoesNotExist:
            return Response("Does not exist")

        return Response(status=status.HTTP_204_NO_CONTENT)


class BulletinViev(APIView):
    def post(self, request):
        voter = Voter.objects.get(voter_uuid=request.data['voter_uuid'])
        blank = Blank.objects.get(voting_name=voter.elections_name)
        bulletin = Bulletin.objects.create(voter=voter, elections=blank)
        bulletin.voter_choise = request.data['voter_choise'] 
        bulletin.save()
        # bulletin = Bulletin(
        #     voter = request.data['voter'],
        #     elections = request.data['elections'],
        #     downloaded = request.data['downloaded'],
        #     voter_choise = request.data['voter_choise']
        # )
        # bulletin.save()
        serializer = BulletinSerializer(bulletin)
        return Response(serializer.data)

    def get(self, request):
        # voter = Voter.objects.get(voter_uuid=request.data['voter_uuid'])
        # bulletin = voter.bulletin
        # bulletin.downloaded = True
        # serializer = BulletinSerializer(bulletin)
        bulletin = Bulletin.objects.all()
        serializer = BulletinSerializer(bulletin, many=True)
        return Response(serializer.data)

    def delete(self, request):
        try:
            Bulletin.objects.all().delete()
        except Bulletin.DoesNotExist:
            return Response("Does not exist")

        return Response(status=status.HTTP_204_NO_CONTENT)