from .serializers import BagSerializer
from rest_framework import generics
from .models import Bag


class BagApi(generics.ListAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer


class BagCreateApi(generics.CreateAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer


class BagUpdateApi(generics.UpdateAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer


class BagDeleteApi(generics.DestroyAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer


class BagReteriveApi(generics.RetrieveAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer
