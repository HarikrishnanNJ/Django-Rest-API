from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from . models import user
from . serializers import std


class listcreate(ListCreateAPIView):
    queryset=user.objects.all()
    serializer_class=std
    
class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset=user.objects.all()
    serializer_class=std   