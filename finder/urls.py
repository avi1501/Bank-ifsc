from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("bank-detail/", views.bank_detail, name='from_ifsc'),

    path("ajax/load_state", views.load_state, name="load_state"),
    path("ajax/load_city", views.load_city, name="load_city"),
    path("ajax/load_dist", views.load_dist, name="load_dist"),
    path("ajax/load_branch", views.load_branch, name="load_branch"),
   
    path("new/", views.new, name="new"),

    path("data/", views.get_ifsc, name="ifsc_data"),
    
]