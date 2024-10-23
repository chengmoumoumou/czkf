from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ScenicSpot, Delicacy


@admin.register(ScenicSpot)
class ScenicSpotAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')  # 可视化列表中显示的字段

@admin.register(Delicacy)
class Delicacy(admin.ModelAdmin):
    list_display = ('name', 'description', 'money')  # 可视化列表中显示的字段
