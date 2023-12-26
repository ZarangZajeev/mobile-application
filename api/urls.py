from django.urls import path
from api import views

urlpatterns=[
    path("mobiles/",views.MobileListCreateView.as_view())
]