from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'trello'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user_detail/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('user_detail/<int:pk>/user_update/', views.UserUpdateView.as_view(), name='user_update'),
    path('lists/create/', views.ListCreateView.as_view(), name='lists_create'),
    path('lists/', views.ListListView.as_view(), name='lists_list'),
    path('lists/<int:pk>/', views.ListDetailView.as_view(), name='lists_detail'),
    path('lists/<int:pk>/update/', views.ListUpdateView.as_view(), name='lists_update'),
    path('lists/<int:pk>/delete/', views.ListDeleteView.as_view(), name='lists_delete'),
    path('cards/create/', views.CardCreateView.as_view(), name='cards_create'),
    path('cards/', views.CardListView.as_view(), name='cards_list'),
    path('cards/<int:pk>/', views.CardDetailView.as_view(), name='cards_detail'),
    path('cards/<int:pk>/update/', views.CardUpdateView.as_view(), name='cards_update'),
    path('cards/<int:pk>/delete/', views.CardDeleteView.as_view(), name='cards_delete'),
    path('cards/create/<int:list_pk>/', views.CardCreateFromHomeView.as_view(), name='cards_create_from_index')
]

