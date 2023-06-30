from .models import Intro
from .serializers import IntroSerializer
from rest_framework import generics

class IntroApi(generics.ListAPIView):
    queryset=Intro.objects.all()
    serializer_class=IntroSerializer

class IntroCreateApi(generics.CreateAPIView):
    queryset=Intro.objects.all()
    serializer_class=IntroSerializer

class IntroDeleteApi(generics.DestroyAPIView):
    queryset=Intro.objects.all()
    serializer_class=IntroSerializer

class IntroUpdateApi(generics.UpdateAPIView):
    queryset=Intro.objects.all()
    serializer_class=IntroSerializer

class IntroReteriveApi(generics.RetrieveAPIView):
    queryset=Intro.objects.all()
    serializer_class=IntroSerializer
    
