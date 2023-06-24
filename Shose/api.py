from .serializers import ShoseSerializer
from rest_framework import generics
from .models import Shoes


class ShoesApi(generics.ListAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoseSerializer


class ShoesCreateApi(generics.CreateAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoseSerializer


class ShoesUpdateApi(generics.UpdateAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoseSerializer


class ShoesDeleteApi(generics.DestroyAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoseSerializer


class ShoesReteriveApi(generics.RetrieveAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoseSerializer
