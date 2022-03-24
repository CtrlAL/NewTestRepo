from django.urls import path
from .views import ResponsibleRepresentativeViev, verify, BulletinViev, BlankViev, VoterViev

urlpatterns = [
    path('RR', ResponsibleRepresentativeViev.as_view()),
    path('RR/<int:id>', ResponsibleRepresentativeViev.as_view()),
    path('RR/verify\\<uuid>', verify, name='verify'),
    path('Blank/<int:id>', ResponsibleRepresentativeViev.as_view()),
    path('Blank/', BlankViev.as_view()),
    path('Voter/', VoterViev.as_view()),
    path('Bulletin/', BulletinViev.as_view()),
]
