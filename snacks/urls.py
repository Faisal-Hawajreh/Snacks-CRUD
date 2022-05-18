from django.urls import path
from .views import (SnackListView,
                    HomePageView,
                    SnackDetailView,
                    SnackCreateView,
                    SnackDeleteView,
                    SnackUpdateView)

urlpatterns = [
    path('',HomePageView.as_view() , name= 'home'),
    path('snacks-list',SnackListView.as_view() , name= 'snacks_list'),
    path('snack-detail/<int:pk>',SnackDetailView.as_view() , name= 'snack_detail'),
    path('create/',SnackCreateView.as_view() , name= 'snack_create'),
    path('<int:pk>/update/',SnackUpdateView.as_view() , name= 'snack_update'),
    path('<int:pk>/delete/',SnackDeleteView.as_view() , name= 'snack_delete'),
]