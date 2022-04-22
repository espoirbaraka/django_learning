from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from employee import views

urlpatterns =[
    path('poste-list', views.posteList),
    path('poste-create', views.posteCreate),
    path('detail-post/<str:pk>/', views.posteDetail),
]