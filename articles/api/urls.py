from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    DuelCreateView, UserListView, DatasetListView, DatasetDetailView, DuelUserListView, DuelDetailView,
    DatasetCreateView, DuelUpdateView, AlgorithmCreateView, AlgorithmListView)

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('create/', ArticleCreateView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
    path('<pk>/update/', ArticleUpdateView.as_view()),
    path('<pk>/delete/', ArticleDeleteView.as_view()),

    path('duel/create/', DuelCreateView.as_view()),
    path('duel/user/', DuelUserListView.as_view()),
    path('duel/<pk>', DuelDetailView.as_view()),
    path('duel/<pk>/update/', DuelUpdateView.as_view()),

    path('dataset/', DatasetListView.as_view()),
    path('dataset/<pk>', DatasetDetailView.as_view()),
    path('dataset/create/', DatasetCreateView().as_view()),

    path('algorithm/create/', AlgorithmCreateView().as_view()),
    path('algorithm/', AlgorithmListView.as_view()),


    path('user/', UserListView.as_view()),
]
