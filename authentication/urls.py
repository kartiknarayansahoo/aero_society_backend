from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('alumni/', views.alumni_list, name='alumni_list'),
    path('alumni/<int:id>/', views.alum_profile, name='alum_profile'),
]
