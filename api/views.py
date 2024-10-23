import hashlib
import os
import urllib


from urllib import response

from aiohttp.web_fileresponse import FileResponse, content_type
from django.views import View
from django.shortcuts import render
 # 或根据你的目录结构调整

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import firstpart
from app import settings
import os





class LoginView (APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        return Response({"status":True},status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return Response({"message": "Use POST to log in."}, status=status.HTTP_200_OK)
# Create your views here.
from django.http import JsonResponse, Http404, HttpResponse
import requests


def get_weather(cityname):#接口
    key = '1c9e474cbd03092f5bea1a3199d781fa'
    api = 'http://apis.juhe.cn/simpleWeather/query'

    params = {
        'key': key,
        'city': cityname,
    }

    response = requests.get(api, params=params)

    try:
        json_data = response.json()
    except ValueError:
        return {'error': '无法解析响应'}

    result = json_data.get('result')
    if result is None:
        return {'error': '没有该城市的天气数据'}

    realtime = result.get('realtime')
    if realtime is None:
        return {'error': '没有实时天气数据'}

    return {
        'city': cityname,
        'temperature': realtime.get('temperature'),
        'info': realtime.get('info'),
    }


def weather_api(request):
    city = request.GET.get('city')
    if city:
        weather_data = get_weather(city)
        return JsonResponse(weather_data)
    return JsonResponse({'error': '请提供城市名'})

# 图文消息
class ImageView(APIView):
    def get(self, request):


            md5 = request.GET.get('md5')

            # 如果提供了 md5，返回特定图片
            if md5:
                imagefile = os.path.join(settings.MEDIA_ROOT, 'images', f'{md5}.png')
                if os.path.exists(imagefile):
                    image_url = os.path.join(settings.MEDIA_URL, 'images', f'{md5}.png').replace('\\', '/')  # 使用正斜杠
                    return JsonResponse({'images': [image_url]})
                else:
                    return JsonResponse({'error': '图片不存在'}, status=404)

            # 返回所有图片
            image_directory = os.path.join(settings.MEDIA_ROOT, 'images')
            images = []

            for filename in os.listdir(image_directory):
                if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):

                    image_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, 'images', filename)).replace('\\', '/')

                    images.append(image_url)

            return JsonResponse({'images': images})

        # if not os.path.exists(imagefile):
        #     raise Http404("Image not found")
        # else:
        #     return HttpResponse(open(imagefile, 'rb'),content_type='image/png')

    def post(self, request, *args, **kwargs):
        # 获取上传的文件
        uploaded_file = request.FILES.get('file')  # 确保前端传递的字段名是 'file'
        if not uploaded_file:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        # 计算文件的 MD5 哈希值
        md5_hash = hashlib.md5()
        for chunk in uploaded_file.chunks():
            md5_hash.update(chunk)

        file_md5 = md5_hash.hexdigest()

        # 构造文件保存的路径
        file_path = os.path.join(settings.MEDIA_ROOT,'images', f"{file_md5}.png")

        # 保存文件到指定目录
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        return JsonResponse({'message': 'File uploaded successfully!', 'md5': file_md5}, status=201)

    def delete(self,request):

        path = request.GET.get('path') or request.data.get('path')

        if not path:
            return JsonResponse(data={'error': '缺少path参数'}, status=400)
        full_path = os.path.join(settings.MEDIA_ROOT, path.lstrip('/'))
        print(full_path)  # 打印完整的文件路径
        print(os.path.exists(full_path))
        # 原始字符串


        print(os.path.exists(full_path))  # 这应该返回 True
        if os.path.exists(full_path):
            os.remove(full_path)
            message = '文件删除成功'
        else:
            message = '文件未找到'

        return JsonResponse(data=message,safe=False)
pass


#景点功能
from .models import ScenicSpot, Delicacy


def scenic_spot_list(request):
    # 返回所有景点信息的列表
    spots = ScenicSpot.objects.all().values()
    return JsonResponse(list(spots), safe=False)

def scenic_spot_detail(request, spot_id):
    # 返回特定景点的详细信息
    try:
        spot = ScenicSpot.objects.get(pk=spot_id)
        spot_data = {
            "name": spot.name,
            "description": spot.description,
            "history": spot.history,
            "highlights": spot.highlights,
            "open_time": spot.open_time,
            "ticket_info": spot.ticket_info,
            "latitude": spot.latitude,
            "longitude": spot.longitude,
            "image_url": spot.image_url,
            "video_url": spot.video_url,
        }
        return JsonResponse(spot_data)
    except ScenicSpot.DoesNotExist:
        return JsonResponse({"error": "Scenic spot not found."}, status=404)
    #美食推荐
    from .models import Delicacy
def Delicacy_list(request):
        # 返回所有景点信息的列表
    Delicacys= Delicacy.objects.all().values()
    return JsonResponse(list(Delicacys), safe=False)







