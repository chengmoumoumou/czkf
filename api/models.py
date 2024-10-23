from django.db import models

# Create your models here.
# models.py
from django.db import models

class ScenicSpot(models.Model):
    name = models.CharField(max_length=100)  # 景点名称
    description = models.TextField()         # 景点描述
    history = models.TextField()             # 历史背景
    highlights = models.TextField()          # 特色亮点
    open_time = models.CharField(max_length=50)  # 开放时间
    ticket_info = models.CharField(max_length=100)  # 门票信息
    latitude = models.FloatField()           # 纬度
    longitude = models.FloatField()          # 经度
    image_url = models.URLField()            # 景点图片URL
    video_url = models.URLField(blank=True, null=True)  # 景点视频URL，可选


class Delicacy (models.Model):
    name=models.CharField(max_length=20)      # 美食名称
    description = models.TextField()          # 美食描述
    image_url = models.URLField()             # 美食图片URL
    money=models.CharField(max_length=50)     #美食价格

    def __str__(self):
        return self.name
