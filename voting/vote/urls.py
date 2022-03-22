from django.urls import path
from .views import ResponsibleRepresentativeViev

urlpatterns = [
    path('RR', ResponsibleRepresentativeViev.as_view()),
    path('RR/<int:id>', ResponsibleRepresentativeViev.as_view()),
    path('Blank/', ResponsibleRepresentativeViev.as_view()),
    path('Blank/<int:id>', ResponsibleRepresentativeViev.as_view()),
]
