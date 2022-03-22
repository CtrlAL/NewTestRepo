from vote.serializers import RRSerializer, BlankSerializer
import uuid
from rest_framework import status
from .models import Blank, ResponsibleRepresentative
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.core.mail import send_mail
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
        send_mail("someting", "somethingmassage",from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=["sasha.lartsev@gmail.com"],fail_silently=False)
        rr_id = uuid.uuid4()
        print(rr_id)
        rr = ResponsibleRepresentative(mail,rr_id)
        rr.save()
        return Response("Hi My Frendo")

    def put(self, request):
        rr = ResponsibleRepresentative.objects.get(pk=request.data['uuid'])
        alphabet = string.ascii_letters + string.digits 
        rr.password = ''.join(secrets.choice(alphabet) for i in range(8))
        rr.save()
        serializer = RRSerializer(rr)
        return Response(serializer.data)


class BlankViev(APIView):
    def get(self, request):
        blank = Blank.objects.all()
        serializer = RRSerializer(blank, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = BlankSerializer(request.data, partial=True)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)



    def put(self, request):
        return Response("Hi my Frendo")


    def delete(self, request):
        return Response("Hi my Frendo")


    
class VoterViev(APIView):
    def get(self, request):
        return Response("Hi my Frendo")


    def post(self, request):
        return Response("Hi my Frendo")


    def put(self, request):
        return Response("Hi my Frendo")


    def delete(self, request):
        return Response("Hi my Frendo")