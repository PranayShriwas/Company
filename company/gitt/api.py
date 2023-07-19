from .models import Git
from rest_framework import generics
from .serializers import GitSerializer


class GitApi(generics.ListAPIView):
    queryset=Git.objects.all()
    serializer_class=GitSerializer

class GitCreateApi(generics.CreateAPIView):
    queryset=Git.objects.all()
    serializer_class=GitSerializer

class GitUpdateApi(generics.UpdateAPIView):
    queryset=Git.objects.all()
    serializer_class=GitSerializer

class GitDeleteApi(generics.DestroyAPIView):
    queryset=Git.objects.all()
    serializer_class=GitSerializer

class GitReteriveApi(generics.RetrieveAPIView):
    queryset=Git.objects.all()
    serializer_class=GitSerializer
