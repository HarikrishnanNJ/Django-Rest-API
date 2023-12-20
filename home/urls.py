from django.urls import path
from . views import PersonListCreateView,PersonDetailView


urlpatterns = [
   
    path('',PersonListCreateView,name='person-list-create'),
    path('person/<pk>/',PersonDetailView,name='person_details'),
 
]