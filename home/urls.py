from django.urls import path
from .  views import StudentDetailView,listcreate

urlpatterns = [
    path('', listcreate.as_view(),name='listcreate'),
    # path('',listapi.as_view(),name='listapi'),
    path('Student/<pk>/' ,StudentDetailView.as_view() , name='student_details' )
]
