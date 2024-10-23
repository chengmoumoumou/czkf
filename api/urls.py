
from django.contrib import admin
from django.urls import path

from django.urls import path, include  # 使用path替代url
from django.conf import settings
from django.conf.urls.static import static

from app import settings
from .views import LoginView, weather_api, ImageView, Delicacy_list
from api import views
from django.urls import path
from .views import scenic_spot_list, scenic_spot_detail
urlpatterns = [

    path('image/', ImageView.as_view(), name='image_view'),
    path('login/',views.LoginView.as_view()),
# urls.py
    path('spots/', scenic_spot_list, name='scenic_spot_list'),
    path('spots/<int:spot_id>/', scenic_spot_detail, name='scenic_spot_detail'),
    path('Delicacy/',Delicacy_list,name='Delicacy_list')





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



