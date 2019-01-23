from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from rest_framework.response import Response

from duels.models import Duel, Dataset, Algorithm
from .serializers import DuelSerializer, UserSerializer, DatasetSerializer, AlgorithmSerializer


class UserListView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        UserListView.queryset = User.objects.all().exclude(pk=request.user.pk)
        serializer = UserSerializer(UserListView.queryset, many=True)
        return Response(serializer.data)


class DatasetListView(ListAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DatasetDetailView(RetrieveAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['data'] = True
        return context


class DatasetCreateView(CreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DuelCreateView(CreateAPIView):
    queryset = Duel.objects.all()
    serializer_class = DuelSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user2=self.request.user)


class DuelUpdateView(UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Duel.objects.all()
    serializer_class = DuelSerializer

    def perform_create(self, serializer):
        serializer.save(user2=self.request.user)


class DuelUserListView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Duel.objects.all()
    serializer_class = DuelSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['pass_username'] = True
        return context

    # TODO filter duels with same user and dataset
    def get(self, request, *args, **kwargs):
        serializer = DuelSerializer(self.queryset.filter(Q(user1=self.request.user.pk) | Q(user2=self.request.user.pk)),
                                    many=True, context=self.get_serializer_context())
        return Response(serializer.data)


class DuelDeleteView(DestroyAPIView):
    queryset = Duel.objects.all()
    serializer_class = DuelSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DuelDetailView(RetrieveAPIView):
    queryset = Duel.objects.all()
    serializer_class = DuelSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['pass_username'] = True
        return context


class AlgorithmCreateView(CreateAPIView):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AlgorithmListView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Algorithm.objects.all().filter(pk__gte=1, pk__lte=8)
    serializer_class = AlgorithmSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['include_algorithm_name'] = True
        return context